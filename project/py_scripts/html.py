from styles import CSS

HTML_PAGE = f"""<!DOCTYPE html>
<html>
<head>
  <title>Warehouse Robot Dashboard</title>
  <style>{CSS}</style>
</head>
<body>
  <nav class="navbar">
    Warehouse Robot Control Panel
  </nav>

  <h2>Select a Task</h2>
  <form method="GET">
    <button class="task" name="task" value="aisle1">Aisle 1</button>
    <button class="task" name="task" value="aisle2">Aisle 2</button>
    <button class="task" name="task" value="aisle3">Aisle 3</button>
    <button class="task" name="task" value="aisle4">Aisle 4</button>
    <button class="task" name="task" value="aisle5">Aisle 5</button>
    <button class="task" name="task" value="aisle6">Aisle 6</button>
    <button class="stop" name="task" value="stop">STOP</button>
  </form>

  <h2>Status</h2>
  <p><strong>Obstacle Distance:</strong> [distance] cm</p>
  <p><strong>Last Speed:</strong> [speed]</p>
</body>
</html>
"""

LOGIN_PAGE = f"""<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="login-container">
    <h1>Login</h1>
    <form method="POST" action="/">
      <input type="text" name="email" placeholder="Email">
      <input type="password" name="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
  </div>
</body>
</html>
"""

SUCCESS_REDIRECT_PAGE = """<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; url=/" />
  <title>Redirecting...</title>
</head>
<body>
  <p>Login successful. Redirecting to dashboard...</p>
</body>
</html>
"""
