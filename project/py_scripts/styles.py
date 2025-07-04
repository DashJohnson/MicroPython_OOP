CSS = """
:root {
  --bg-dark: #121212;
  --bg-panel: #1e1e1e;
  --primary: #3498db;
  --danger: #e74c3c;
  --text-light: #f0f0f0;
  --button-radius: 12px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
  background: var(--bg-dark);
  color: var(--text-light);
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  flex-direction: column;
}

.navbar {
  background: var(--bg-panel);
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--primary);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  margin-bottom: 30px;
  width: 100%;
  max-width: 800px;
}

h2 {
  margin: 20px 0;
  font-size: 1.3rem;
  color: #ddd;
}

form {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
}

button {
  background: var(--primary);
  border: none;
  border-radius: var(--button-radius);
  color: white;
  font-size: 1rem;
  padding: 16px 28px;
  min-width: 130px;
  transition: all 0.25s ease;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
button:hover {
  background: #2980b9;
  transform: scale(1.05);
}
button:active {
  transform: scale(0.98);
}

.stop {
  background: var(--danger);
}
.stop:hover {
  background: #c0392b;
}

.login-container {
  background: var(--bg-panel);
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.4);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.login-container h1 {
  color: var(--primary);
  margin-bottom: 24px;
}

.login-container input {
  width: 100%;
  padding: 12px;
  margin: 12px 0;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
}

.login-container button {
  width: 100%;
  margin-top: 12px;
}
"""
