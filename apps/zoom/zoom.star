load("render.star", "render")
load("animation.star", "animation")
load("pixlib/input.star", "input")

def main():
  data = input.json()
  in_meeting = data.get("in_meeting", False)

  if not in_meeting:
    return []

  muted = data.get("muted")

  frames = animation.Transformation(
    duration=60,
    keyframes=[],
    wait_for_child=False,
    child=render.Box(
      child=render.Text(
        "ON AIR",
        font="10x20",
        color=("#00ff00" if muted else "#ff0000"),
      )
    )
  )

  root = render.Root(
    delay=1000,
    child=frames
  )
  return root

