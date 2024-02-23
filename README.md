<p align="center">

![Pixbyt logo](logo.png)

</p>

<span align="center">

# Reimagine what your Tidbyt can do

**Pixbyt is a self-hosted [Tidbyt](https://tidbyt.com) app server for advanced apps**<br>
that aren't supported by the official [community app](https://tidbyt.dev/docs/publish/community-apps) server<br>
that you can access through Tidbyt's mobile app.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/DouweM/pixbyt)

</span>

---

<table>
  <tr>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-crossword">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-crossword/main/screenshot.webp" width="174"><br>
        crossword
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-jeopardy">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-jeopardy/main/screenshot.webp" width="174"><br>
        jeopardy
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-common-misconceptions">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-common-misconceptions/main/screenshot.webp" width="174"><br>
        common-misconceptions
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-owen-wilson-facts">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-owen-wilson-facts/main/screenshot.webp" width="174"><br>
        owen-wilson-facts
      </a>
    </td>
  </tr>
  <tr>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-plex">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-plex/main/screenshot.webp" width="174"><br>
        plex
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-apple-tv">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-apple-tv/main/screenshot.webp" width="174"><br>
        apple-tv
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/rspeicher/tidbyt-letterboxd">
        <img src="https://raw.githubusercontent.com/rspeicher/tidbyt-letterboxd/main/screenshot.webp" width="174"><br>
        letterboxd
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-parcelapp">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-parcelapp/main/screenshot.webp" width="174"><br>
        parcelapp
      </a>
    </td>
  </tr>
  <tr>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-homebridge-unifi">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-homebridge-unifi/main/screenshot.webp" width="174"><br>
        homebridge-unifi
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-guess-the-flag">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-guess-the-flag/main/screenshot.webp" width="174"><br>
        guess-the-flag
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-ffmpeg">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-ffmpeg/main/screenshot.webp" width="174"><br>
        ffmpeg
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-revolution">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-revolution/main/screenshot.webp" width="174"><br>
        revolution
      </a>
    </td>
  </tr>
  <tr>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/pixbyt/tree/main/apps/hello-world">
        <img src="https://raw.githubusercontent.com/DouweM/pixbyt/main/apps/hello-world/screenshot.webp" width="174"><br>
        hello-world
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/rspeicher/tidbyt-dadjoke">
        <img src="https://raw.githubusercontent.com/rspeicher/tidbyt-dadjoke/main/screenshot.webp" width="174"><br>
        dadjoke
      </a>
    </td>
    <td valign="top" align="center" width="25%">
      <a href="https://github.com/DouweM/tidbyt-speedtest">
        <img src="https://raw.githubusercontent.com/DouweM/tidbyt-speedtest/main/screenshot.webp" width="174"><br>
        speedtest
      </a>
    </td>
    <td valign="center" align="center" width="25%">
      <a href="#option-c-create-a-brand-new-app">
        <strong>Your next Tidbyt app</strong>
      </a>
    </td>
  </tr>
</table>

---

Your Tidbyt does not run apps directly; it depends on a server to periodically run apps and push the resulting images to the device.
When you install a [community app](https://tidbyt.dev/docs/publish/community-apps) through Tidbyt's mobile app, the app runs on Tidbyt's official app server.
For security reasons, there are a ton of limitations on what these apps are allowed to do, which means some awesome app ideas are impossible to implement.

Apps running on Pixbyt have none of these limitations:
- [x] Run **Python scripts and packages**, not just Starlark applets
- [x] Reach **local network resources**, not just the public internet
- [x] Work with **complex APIs**, not just simple REST HTTP requests
- [x] Read **local files**, like images or JSON
- [x] Organize your source code across **multiple modules**

Pixbyt lets you realize your wildest Tidbyt dreams by making it easy to:
- **build** advanced Tidbyt apps,
- **install** advanced apps built by the community,
- **manage** multiple Tidbyts and apps,
- **package** apps together in a [Docker](https://www.docker.com/) image, and
- **launch** the app server using [Docker Compose](https://docs.docker.com/compose/).

## How it works

Pixbyt's advanced features are enabled by [`tap-pixlet`](https://github.com/DouweM/tap-pixlet), an unofficial Tidbyt app runner that extends [Pixlet](https://github.com/tidbyt/pixlet) (the official Tidbyt app development framework) with an unofficial standard library named [Pixlib](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib), similar to how [Starlib](https://github.com/qri-io/starlib) is the unofficial standard library for [Starlark](https://github.com/google/starlark-go) (the Python-like language Tidbyt apps are written in).
Pixlib comes with functions like
[`file.read`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibfile),
[`file.exec`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibfile),
[`font.height`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibfont),
[`html.unescape`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibhtml), and
[`html.xpath`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibhtml),
helpful constants like
[`const.WIDTH`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibconst),
[`const.HEIGHT`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibconst), and
[`const.FPS`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibconst), and
overloads [`load`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#load) to support local modules.

Pixbyt uses
`tap-pixlet` to run apps,
[`target-tidbyt`](https://github.com/DouweM/target-tidbyt) and [`target-webp`](https://github.com/DouweM/target-webp) to push the resulting images to your Tidbyt or WebP image files,
[Airflow](https://airflow.apache.org/) to run apps on a schedule, and
[Meltano](https://github.com/meltano/meltano) to tie these components together.
Pixbyt also includes resources to [package your apps into a Docker image](./Dockerfile) (locally or [automatically on GitHub Actions](./.github/workflows/main.yml)) and [launch it using Docker Compose](./docker-compose.yml).

## Try it out

This repo defines a Pixbyt app server with a single [`hello-world` app](./apps/hello-world) that shows off some of its advanced features.
It automatically builds a [`ghcr.io/douwem/pixbyt:main` Docker image](https://github.com/DouweM/pixbyt/pkgs/container/pixbyt) that can be [launched using Docker Compose](./docker-compose.yml) to render the app to a Tidbyt device every hour:

<img src="https://raw.githubusercontent.com/DouweM/pixbyt/main/apps/hello-world/screenshot.webp" width="174">

To quickly see Pixbyt in action, you can open this repo in GitHub Codespaces and render the `hello-world` app to a WebP image or your own Tidbyt before you add your own apps.
Codespaces will automatically install the necessary dependencies and launch you into a web-based VS Code editor.

1. Click the green "Use this template" button at the top of this page
1. Choose "Open in a codespace" and wait for the codespace to start
1. Optionally, update the `HELLO_WORLD_NAME` environment variable in `.env` to replace `world` with your own name.
1. Render app to a WebP image file:

    ```bash
    TAP_PIXLET_MAGNIFICATION=8 meltano run hello-world--webp
    ```

    The image will be created at `output/hello-world/<timestamp>.webp`.
    The exact path is also printed in the command output.
1. Render app to your Tidbyt:
   1. Find your Device ID and Key in the Tidbyt mobile app under Settings > General > Get API Key.
   1. Update the `TIDBYT_DEVICE_ID` and `TIDBYT_KEY` environment variables in `.env`.
   1. Render the `hello-world` app and send it to your Tidbyt (in the foreground):

       ```bash
       TAP_PIXLET_BACKGROUND=false meltano run hello-world
       ```

## Set up your own

When you're ready to start using apps other than `hello-world`, follow the steps below to build your own Pixbyt app server using this repo as a template:

### 1. Create your own Pixbyt repo

#### Option A: GitHub Codespaces

If you've already opened this template repo in a codespace using the steps above:

1. Click the "Source Control" icon in the sidebar
2. Click "Publish" <!-- TODO: Ensure steps are correct -->

If you haven't launched a codespace yet:
1. Click the green "Use this template" button at the top of this page
1. Choose "Open in a codespace"

<details>
<summary>

#### Option B: Build locally

</summary>

1. Click the green "Use this template" button at the top of this page
1. Choose "Create a new repository"
1. Create a new (private) repo
1. Clone your new repository and enter the new directory:

    ```bash
    git clone git@github.com:<username>/pixbyt.git
    cd pixbyt
    ```

</details>

### 2. Configure Pixbyt

1. If the `.env` configuration file doesn't exist yet, create it from the sample:
   ```bash
   cp .env.sample .env
   ```
1. Update the `TZ` environment variable in `.env` to your ["TZ" timezone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). This is used by many apps that show the (relative) date and time.

#### Option A: Configure just one Tidbyt

1. Find your Device ID and Key in the Tidbyt mobile app under Settings > General > Get API Key.
1. Update the `TIDBYT_DEVICE_ID` and `TIDBYT_KEY` environment variables in `.env`.

<details>
<summary>

#### Option B: Configure multiple Tidbyts

</summary>

1. If `devices.yml` doesn't exists yet, create it from the sample:
   ```bash
   cp devices.yml.sample devices.yml
   ```
1. For each device:
   1. Add the device to `devices.yml` under `devices:`:
       ```yaml
       devices:
       # ...
       - name: <name>
         id: $TIDBYT_<NAME>_DEVICE_ID
         key: $TIDBYT_<NAME>_KEY
       ```

       1. Replace `<name>` with the room name or another identifier.
       1. Replace `<NAME>` with the uppercased version thereof.

       For example:

       ```yaml
       devices:
       # ...
       - name: office
         id: $TIDBYT_OFFICE_DEVICE_ID
         key: $TIDBYT_OFFICE_KEY
       ```
   1. Find your Device ID and Key in the Tidbyt mobile app under Settings > General > Get API Key.
   1. Add the `TIDBYT_<NAME>_DEVICE_ID` and `TIDBYT_<NAME>_KEY` environment variables in `.env`.
       For example:

       ```bash
       TIDBYT_OFFICE_DEVICE_ID="foo-bar-baz-qux-abc"
       TIDBYT_OFFICE_KEY="<key>"
       ```

</details>

### 3. Add your apps

The most important files in your Pixbyt repo (and likely the only ones you'll want to edit) are the following, which define the apps, their configuration, and their apps:

```bash
pixbyt
├─ .env                     # Configuration
├─ apps.yml                 # App schedules
├─ devices.yml              # Optional: Devices
└─ apps
   └─ <app>                 # One directory for each app
      ├─ <app>.star         # Main Pixlet applet
      ├─ pixbyt.yml         # Pixbyt metadata
      ├─ requirements.txt   # Optional: Python packages (one `pip install` argument per line)
      ├─ apt-packages.txt   # Optional: APT packages (one `apt-get install` argument per line)
      ├─ *.py               # Optional: Python scripts to run using `file.exec`
      ├─ *.star             # Optional: Starlark files to load using `load`
      └─ *                  # Optional: Files to read using `file.read`
```

Out of the box, Pixbyt comes with a single [`hello-world` app](./apps/hello-world) that shows off some of its advanced features and can be used as an example to build your own.

**If you're just trying out Pixbyt** and don't yet have another app in mind that you'd like to run, you can keep `hello-world` and skip ahead to step 4 to build and launch the app server.

**If you don't want `hello-world`** on your Tidbyt, you can disable it by removing its entry from `apps.yml` (and `.env`), but **DO NOT remove the `apps/hello-world` directory** as the [GitHub Actions workflow](./.github/workflows/main.yml) that builds the Docker image uses it to test if the image works.

#### 3.1. Add an app

##### Option A: Use the example `hello-world` app

Skip ahead to step 4 to build and launch the app server.

<details>
<summary>

##### Option B: Install an existing app

</summary>

1. Add the app's repo as a submodule under `apps`:

    ```bash
    git submodule add https://github.com/<username>/<repository>.git apps/<app>
    ```

    For example, to install [`crossword`](https://github.com/DouweM/tidbyt-crossword):

    ```bash
    git submodule add https://github.com/DouweM/tidbyt-crossword.git apps/crossword
    ```

    Note that in this case, the repo is called `tidbyt-crossword`, but the app directory needs to be called `crossword`.

</details>

<details>
<summary>

##### Option C: Create a brand-new app

</summary>

1. Create a new directory for your app under `apps`, and enter the new directory:

    ```bash
    cd apps
    mkdir <app>
    cd <app>
    ```

1. Create the main applet at `apps/<app>/<app>.star`.

    Any standard [Pixlet](https://github.com/tidbyt/pixlet) applet is supported, as well as all [Pixlib](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib) features.

    Note that the app directory and file names need to match.

    Optionally, your app directory can also contain:
    - `*.py` scripts to run using [`file.exec`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibfile)
    - `*.star` files to load using [`load`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#load)
    - arbitrary files to read using [`file.read`](https://github.com/DouweM/tap-pixlet/tree/main/tap_pixlet/pixlib#pixlibfile)
    - Python packages in `requirements.txt` (one `pip install` argument per line)
    - APT packages in `apt-packages.txt`(one `apt-get install` argument per line)

1. Create the Pixbyt metadata file at `apps/<app>/pixbyt.yml`:

    ```yaml
    jobs:
    - name: <app>
      tasks:
      - tap-pixlet--<app> target-tidbyt
    - name: <app>--webp
      tasks:
      - tap-pixlet--<app> target-webp

    plugins:
      extractors:
      - name: tap-pixlet--<app>
        inherit_from: tap-pixlet
        # TODO: If your app does not have a `requirements.txt` defining Python packages, delete the following line:
        pip_url: git+https://github.com/DouweM/tap-pixlet.git -r apps/<app>/requirements.txt
        config:
          path: apps/<app>
          # TODO: If your app does not require configuration, delete the following lines:
          app_config:
            # TODO: For any key your app reads from `config`, add an entry mapping the lowercase key to an uppercase environment variable, e.g. `name: $HELLO_WORLD_NAME`:
            <key>: $<APP>_<KEY>
      ```

      Most of this is boilerplate for [Meltano](https://docs.meltano.com/concepts/project), you only need to make the following changes:

      1. Replace `<app>` with the name of your app
      1. Follow the `TODO` instructions.

</details>

#### 3.2. Configure the app

1. Add the app and its update schedule to `apps.yml` under `apps:`:

    ```yaml
    apps:
    # ...
    - name: <app>
      schedule: '<cron expression>'
      # If you have multiple Tidbyts defined in `devices.yml`, you can optionally filter them by name:
      # devices: [<device>]
    ```

    1. Replace `<app>` with the name of the app.
    1. Replace `<cron expression>` with an appropriate [cron expression](https://crontab.guru/):

         - Clocks should use `* * * * *` to update every minute, so that the displayed time is always as fresh as possible.
         - Apps that display a random entry from a list can use `*/5 * * * *` to update every 5 minutes, so that a fresh entry is shown on every app rotation.
         - Apps that show the latest data from some API can use `*/15 * * * *` to update every 15 minutes, or something else appropriate for your data source and the expected data freshness.
         - Apps that will always generate the same image can use `0 0 * * *` to update every day at midnight, just to be sure.

         A recommended schedule is typically documented in the app's `README`.
    1. Optionally, replace `<device>` with the name of a device defined in `devices.yml` to only send the app to that device. By default, the app will be sent to all devices.

    For example:

    ```yaml
    apps:
    # ...
    - name: hello-world
      schedule: '0/15 * * * *' # Every 15 minutes
      devices: [office] # Optional
    ```

    Note that examples in apps' `README`s sometimes use `schedules` and `interval` keys instead of `apps` and `schedules`. They are equivalent and both are supported, but the latter is preferred.

1. If the app requires configuration, add its environment variables to `.env`:

    For any config key the app defines under `app_config:` in its `pixbyt.yml` file, add a value for the uppercase environment variable:

    ```bash
    <APP>_<KEY>="<value>"
    ```

    The exact environment variables are typically documented in the app's `README`.

    For example:

    ```bash
    HELLO_WORLD_NAME="world"
    ```

#### 3.3 Test the app

If you're developing a new app, or you're not confident you've configured it correctly, you can test it without building and running the entire app server by following the [Development](#how-to-develop-apps-with-pixbyt) instructions below.

### 4. Build the app server

To be able to easily run your app server using Docker Compose, you will build a Docker image from your repo containing Pixbyt and your apps.

<details>
<summary>

#### Option A: Build using GitHub Actions

</summary>

1. Edit `docker-compose.yml`:
   1. Under `x-remote-image:`, replace `<username>` with your GitHub username
   2. Under `pixbyt:`, comment out `<<: *local-image` and uncomment `<<: *remote-image` on the next line

1. Commit your changes:

    ```bash
    git add -A
    git commit -m "Set up my Pixbyt"
    ```

1. Push your repo up to GitHub:

    ```bash
    git push origin main
    ```

    This will automatically trigger a GitHub Actions workflow to build a Docker image containing Pixbyt and your apps whenever your apps or their schedules change.

</details>

<details>
<summary>

#### Option B: Build locally

</summary>

Note that you'll need to do this each time your apps or their schedules change.

1. Ensure [Docker](https://www.docker.com/) is installed.

  Note that Docker is not available in GitHub Codespaces.
  If you've opened your Pixbyt repo in GitHub Codespaces, use the GitHub Actions method above instead.

1. Build a Docker image containing Pixbyt and your apps:

    ```bash
    docker compose build
    ```

</details>

### 5. Launch the app server

During testing and development, you can do this on your local machine.
In production, you'll likely want to do this on a NAS or other homelab, or on any other (virtual) server that has access to the required network resources.

Note that you'll need to do this each time your apps or their schedules change and a new Docker image is built, or whenever their configurations change.

1. Ensure [Docker](https://www.docker.com/) is installed.
1. If you chose to build your Docker image using GitHub Actions in the previous step, [authenticate with the GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic).
1. Create or update `.env` with your configuration, based on [the sample](./.env.sample) or the configuration you used during development.
1. Launch Pixbyt using Docker Compose:

    ```bash
    docker compose up --pull --build -d
    ```

Your Pixbyt app server is now running, and your apps will update on schedule!
You can find logs for your apps under `logs/apps/<app>/`.

## How to develop apps with Pixbyt

During app development or debugging, you will not want to build the entire Docker image each time your apps, their schedules, or their configurations change, nor will you want to run the entire app server.

Instead, you can directly render a specific app to a WebP image file or your Tidbyt, and quickly iterate on your app based on what you see in the logs and the output image.

### Set up development environment

#### Option A: GitHub Codespaces

The quickest way to start developing is using GitHub Codespaces, which will automatically install the necessary dependencies and launch you into a web-based VS Code editor.

If you're already inside a codespace, continue to the next step.

If you've already created your own repo using this template repo:

1. Click the "`<>` Code" button at the top of the page
1. Choose "Codespaces" > "Create codespace on main"

If you haven't created a new repo from this template yet:

1. Click the green "Use this template" button at the top of this page
1. Choose "Open in a codespace"

<details>
<summary>

#### Option B: Develop locally

</summary>

1. Install [Pixlet](https://github.com/tidbyt/pixlet):

    - On macOS:

      ```bash
      brew install tidbyt/tidbyt/pixlet
      ```

    - [Other operating systems](https://tidbyt.dev/docs/build/installing-pixlet)

1. Install [Meltano](https://github.com/meltano/meltano):

   - With `pip`:

      ```bash
      pip install meltano
      ```

   - [Other installation methods](https://docs.meltano.com/getting-started/installation)

1. If your project contains [apps as submodules](#31-add-an-app), initialize them:

    ```bash
    git submodule update --init
    ```

1. Manually install any APT packages defined in your apps' `apt-packages.txt` files.

1. Install [`tap-pixlet`](https://github.com/DouweM/tap-pixlet), [`target-tidbyt`](https://github.com/DouweM/target-tidbyt), and [`target-webp`](https://github.com/DouweM/target-tidbyt) using Meltano:

    ```bash
    meltano install
    ```

</details>
<details>
<summary>

#### Option C: Docker image

</summary>

If you've already built a Docker image and want to test the apps inside it without making changes to them, you can use the `docker compose` commands below.

</details>

### Render app to a WebP image file

The image will be created at `output/<app>/<timestamp>.webp`.
The exact path is also printed in the command output.

#### Regular size (64x32)

```bash
meltano run <app>--webp

# Using Docker image:
docker compose run pixbyt run <app>--webp
```

For example:

```bash
meltano run hello-world--webp

# Using Docker image:
docker compose run pixbyt run hello-world--webp
```

#### Magnified 8 times (512x256)

```bash
TAP_PIXLET_MAGNIFICATION=8 meltano run <app>--webp

# Using Docker image:
docker compose run -e TAP_PIXLET_MAGNIFICATION=8 pixbyt run <app>--webp
```

For example:

```bash
TAP_PIXLET_MAGNIFICATION=8 meltano run hello-world--webp

# Using Docker image:
docker compose run -e TAP_PIXLET_MAGNIFICATION=8 pixbyt run hello-world--webp
```

### Render app to your Tidbyt

#### Send to foreground

The app will immediately show up on your Tidbyt.
This is useful during development.

```bash
TAP_PIXLET_BACKGROUND=false meltano run <app>

# Using Docker image:
docker compose run -e TAP_PIXLET_BACKGROUND=false pixbyt run <app>
```

For example:

```bash
TAP_PIXLET_BACKGROUND=false meltano run hello-world

# Using Docker image:
docker compose run -e TAP_PIXLET_BACKGROUND=false pixbyt run hello-world
```

#### Send to background

The app will be added to the Tidbyt app rotation.
This is useful when you're running this command on a schedule, to make sure that the app will be up to date the next time it comes up in the app rotation.

```bash
meltano run <app>

# Using Docker image:
docker compose run pixbyt run <app>
```

For example:

```bash
meltano run hello-world

# Using Docker image:
docker compose run pixbyt run hello-world
```

### Keep apps up to date

If you're working with Pixbyt in GitHub Codespaces or locally, you can quickly iterate on apps and test your changes (this is not possible when you're debugging inside a Docker container).
Changes to an app's source files are automatically picked up, but changes to APT and Python package dependencies aren't.

If an app defines Python packages in its `requirements.txt` file, you'll need to manually do a clean install of the app's Meltano plugin every time it changes:

```bash
meltano install --clean extractor tap-pixlet--<app>
```

For example:

```bash
meltano install --clean extractor tap-pixlet--hello-world
```

If an app defines APT packages in its `apt-packages.txt` file, you'll need to manually install them every time they change.
