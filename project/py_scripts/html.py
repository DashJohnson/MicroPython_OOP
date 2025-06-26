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
</body>
</html>
"""
