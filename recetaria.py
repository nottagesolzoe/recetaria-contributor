#!/usr/bin/env python3
"""Offline draft validation and explicit, artifact-specific consent. No network."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def validate(value, schema, path='$'):
    """Validate the deliberately bounded subset used by the bundled schema.

    Fail closed on unknown keywords; not a general JSON Schema implementation.
    """
    supported = {'$schema', 'title', 'description', 'type', 'const', 'enum', 'required',
                 'properties', 'additionalProperties', 'minLength', 'minimum',
                 'maximum', 'items', 'minItems'}
    if set(schema) - supported:
        raise ValueError(f'{path}: unsupported schema keywords')
    if 'const' in schema and (type(value) is not type(schema['const']) or value != schema['const']):
        raise ValueError(f'{path}: invalid fixed value')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{path}: invalid choice')
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str, 'integer': int,
             'boolean': bool, 'null': type(None)}
    if kind is not None:
        if kind not in types or type(value) is not types[kind]:
            raise ValueError(f'{path}: expected {kind}')
    if kind == 'object':
        missing = set(schema.get('required', [])) - value.keys()
        extra = value.keys() - schema.get('properties', {}).keys()
        if missing or (schema.get('additionalProperties') is False and extra):
            raise ValueError(f'{path}: missing or unexpected fields')
        for key, item in value.items():
            if key in schema.get('properties', {}):
                validate(item, schema['properties'][key], path+'.'+key)
    elif kind == 'array':
        if len(value) < schema.get('minItems', 0):
            raise ValueError(f'{path}: empty list')
        for i, item in enumerate(value):
            validate(item, schema['items'], f'{path}[{i}]')
    elif kind == 'string':
        if len(value.strip()) < schema.get('minLength', 0):
            raise ValueError(f'{path}: empty text')
    elif kind == 'integer':
        if value < schema.get('minimum', value) or value > schema.get('maximum', value):
            raise ValueError(f'{path}: outside allowed range')

def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON keys are not accepted')
        result[key] = value
    return result

def load_draft(path):
    raw = Path(path).read_bytes()
    if len(raw) > 1_000_000:
        raise ValueError('Draft exceeds 1 MB')
    value = json.loads(raw, object_pairs_hook=no_duplicate_keys)
    schema = json.loads((ROOT/'schemas/recipe_draft.schema.json').read_text())
    validate(value, schema)
    return value

def prepare(value, output, confirm=input, display=print):
    # Always obtain fresh consent, even if input claims it already has consent.
    value = json.loads(json.dumps(value))
    value['consent_to_submit'] = True
    value['submitted_at'] = None
    payload = json.dumps(value, ensure_ascii=False, indent=2)+'\n'
    display('Artefacto exacto para RecetArIA. Solo se guardará localmente; no se enviará a Drive.')
    display(payload)
    display('Revisá privacidad, autoría y contenido completo. Modificarlo requiere otra revisión.')
    if confirm('Escribí SUBMIT para preparar esta versión; cualquier otra respuesta cancela: ').strip() != 'SUBMIT':
        return False
    # Exclusive creation prevents accidental replacement of drafts or source files.
    with Path(output).open('x', encoding='utf-8') as stream:
        stream.write(payload)
    return True

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate').add_argument('draft')
    command = sub.add_parser('prepare')
    command.add_argument('draft')
    command.add_argument('--out', required=True)
    args = parser.parse_args()
    try:
        value = load_draft(args.draft)
        if args.command == 'validate':
            print('Formato válido. Esto no acredita privacidad, reproducción ni aprobación editorial.')
        else:
            print('Preparado localmente; no enviado.' if prepare(value, args.out) else 'Cancelado; no se creó el archivo.')
    except (ValueError, OSError, EOFError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
