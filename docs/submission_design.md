# Recepción controlada: pendiente

V0.1 implementa prepare local y una interfaz que falla explícitamente al intentar transporte. No hay endpoint ni acceso a Drive configurados.

Contrato futuro: recibir solo JSON conforme al schema, consent_to_submit true y autoría autenticada. Asignar fecha real de recepción a submitted_at en el servidor. Deduplicar por identidad autenticada, original_recipe_id y recipe_version; conservar recibo e historial. Rechazar campos adicionales, cargas excesivas y cualquier estado editorial no DRAFT/pending. No confiar en identidad, fecha o consentimiento únicamente porque lo dice un JSON.

Ruta administrada por el servidor: RecetArIA/Contributions/[Contributor]/DRAFTS/. Mapear identidad a carpeta sin usar texto libre como ruta. El contribuidor no puede elegir carpetas ni listar o leer Drive. Las credenciales pertenecen solo al servicio de RecetArIA, fuera del paquete y del cliente.

Falta acordar y configurar: autenticación de participantes, cuenta de servicio o autorización del propietario con permisos mínimos, carpeta destino, alojamiento del endpoint, almacenamiento seguro de secretos, límites y protección contra duplicados, recibos, retención/borrado y prueba de aislamiento entre participantes. Antes de habilitar transmisión se debe mostrar destino y carga exacta y renovar confirmación si cambian. Ninguna credencial se necesita para probar detección, escritura o exportación local.
