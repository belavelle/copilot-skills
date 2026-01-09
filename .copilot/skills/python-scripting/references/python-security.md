# Python Security Notes

- Treat all external inputs as untrusted.
- Never commit secrets.
- Avoid eval/exec.
- Prefer subprocess.run([...], check=True) without shell=True.
- Validate paths and inputs.
- Use HTTP timeouts and handle non-2xx responses.
