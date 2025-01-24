# Dotbot apk Plugin

For use with [dotbot](https://github.com/anishathalye/dotbot),
this plugin allows one to easily install or upgrade a list of apk packages.

This plugin is a port of [dotbot-yay](https://github.com/OxSon/dotbot-yay) for use with `apk`, which itself is forked from [dotbot-yaourt](https://github.com/niklas-heer/dotbot-yaourt). Basically the same thing with a `apk` command ran, plus a couple other relevant changes.

[dotbot-yay](https://github.com/OxSon/dotbot-yay) was mostly based on [dotbot-yaourt](https://github.com/niklas-heer/dotbot-yaourt),
[dotbot-yaourt](https://github.com/niklas-heer/dotbot-yaourt) was itself heavily inspired by the [apt-get](https://github.com/rubenvereecken/dotbot-apt-get) plugin.

## Usage

It's easiest to track this plugin in your dotfiles repo:

```bash
git submodule add https://github.com/mnb3000/dotbot-apk
```

The original author also recommends having your apk list in a separate file
since dotbot will need root privileges in order to use the plugin.

If you use the default install script provided by [dotbot](https://github.com/anishathalye/dotbot), using the plugin will look like this:

```bash
./dotbot/bin/dotbot -p dotbot-apk/apk.py -c packages.conf.yaml
```

Using the `install` script provided by this repo, using the plugin will look like this:

```bash
./install packages
```

Example for `packages.conf.yaml`:

```yaml
- apk:
    - vim
    - zsh
    - tldr
```
