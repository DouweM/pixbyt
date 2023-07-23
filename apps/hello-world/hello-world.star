load("render.star", "render")
load("pixlib/const.star", "const")
load("./client.star", "client")

def main(config):
    NAME = config.get("name") or "world"

    image = client.get_image()
    text = client.get_response(NAME)

    return render.Root(
        child=render.Column(
            expanded=True,
            main_align="space_around",
            cross_align="center",
            children=[
                render.Image(src=image, width=const.WIDTH),
                render.Text(text)
            ]
        )
    )
