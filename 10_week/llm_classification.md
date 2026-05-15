LLM 정확도: 0.6300
LLM F1:    0.6942
분류 실패(Unknown): 0건

              precision    recall  f1-score   support

      Normal       0.91      0.38      0.53        56
   Anomalous       0.55      0.95      0.69        44

    accuracy                           0.63       100
   macro avg       0.73      0.66      0.61       100
weighted avg       0.75      0.63      0.60       100

PROMPT_TEMPLATE = 'You are a senior web application security analyst with 10 years of experience.\nClassify the HTTP request as "Normal" or "Anomalous".\nAnomalous includes: SQL Injection, XSS, Path Traversal, Command Injection, brute-force, scanner probes.\n\nExamples:\nRequest: GET /products/list?page=2 HTTP/1.1\nOutput: {{"label": "Normal", "reason": "Standard pagination request"}}\n\nRequest: GET /search?q=<script>alert(1)</script> HTTP/1.1\nOutput: {{"label": "Anomalous", "reason": "XSS attempt via script tag injection"}}\n\nRequest: GET /files?path=../../etc/passwd HTTP/1.1\nOutput: {{"label": "Anomalous", "reason": "Path traversal attempting to read /etc/passwd"}}\n\nRequest: POST /login HTTP/1.1\nBody: username=admin&password=123456\nOutput: {{"label": "Normal", "reason": "Standard login form submission"}}\n\nRequest: GET /search?q=1; DROP TABLE users-- HTTP/1.1\nOutput: {{"label": "Anomalous", "reason": "SQL Injection with DROP TABLE statement"}}\n\nNow classify (respond with JSON only):\nRequest: {http_text}\nOutput:'
