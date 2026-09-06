# Revisión editorial

DETECTED y CANDIDATE son estados locales. KEEP conserva; EDIT modifica; REJECT descarta. SUBMIT expresa la voluntad de ofrecer una versión, sin aprobarla. El archivo permanece DRAFT con editorial_review pending. Solo el sistema editorial de Sol asigna CASI, REHACER o APROBADA y conserva atribución e historial de versiones.

LISTO, REVISAR y NO AVANZAR son diagnósticos de la ejecución de una receta, no decisiones de inclusión en el corpus. La receta aprobada «De una idea de scraping a un corpus que realmente se puede analizar» se reconoce por título; no se dispone de su contenido en este paquete.

## Gate obligatorio de aprobación

APROBADA requiere: trazabilidad al episodio real verificada localmente por el investigador, procedimiento concreto, prueba documentada por otra persona sobre la versión exacta y decisión explícita de Sol. No basta la evaluación del LLM ni pasar validación JSON. Una corrección posterior exige repetir la prueba afectada y vincular el nuevo informe a la receta completa actualizada.

`python3 verify_test.py draft.json test-report.json` comprueba vinculación de versión y estructura mínima del informe. No determina si la evidencia es verdadera ni asigna APROBADA. Sol evalúa la suficiencia y la calidad de la prueba. Para obtener la huella: `python3 verify_test.py draft.json`. El informe queda en el entorno local hasta que su contenido exacto también haya sido autorizado para recepción central; nunca adjuntar chats como evidencia.
