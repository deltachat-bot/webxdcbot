# webxdcbot

Example Delta Chat bot + webxdc app as bot's frontend.

## Install

Clone this repository and run inside the project's folder:

```sh
# first build the webxdc app / frontend:
cd frontend/
npm install
npm run build
cd ..
# install the python package bot / backend:
pip install .
```

### Installing deltachat-rpc-server

This program depends on a standalone Delta Chat RPC server `deltachat-rpc-server` program that must be
available in your `PATH`. To install it check:
https://github.com/deltachat/deltachat-core-rust/tree/master/deltachat-rpc-server

## Configuration

Configure the bot:

```sh
webxdcbot init bot@example.com PASSWORD
```

Start the bot:

```sh
webxdcbot serve
```

Run `webxdcbot --help` to see all available options.

## Usage

1. Write to the bot in Delta Chat, for example send a "hi" message to it
2. The bot will reply with the webxdc app
3. Open the webxdc app and send a message there
4. The bot will reply to you inside the app
