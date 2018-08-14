# ncm2-look.vim

Port of the [neco-look] plugin for [NCM2]

`look` is a BSD binary that comes default with many Linux and macOS
installations that allows you to lookup words. look.vim uses this binary to
provide word completion, useful for writing prose.

look.vim may also use your custom spellfile (See `:h spellfile`) to provide
custom words

![](https://user-images.githubusercontent.com/48519/42656561-0748c44e-85f6-11e8-8f68-aeacda42876b.gif)

## Requirements

-   [ncm2]
-   [nvim-yarp] (required by ncm2)
-   `look` binary. run `which look` on your terminal to see if it's available;

## Installation

Use your favorite plugin manager. I recommend [vim-plug]:

```vim
" NCM  and it's requirements
Plug 'ncm2/ncm2'
Plug 'roxma/nvim-yarp'
" Look.vim completion plugin
Plug 'filipekiss/ncm2-look.vim'


" enable ncm2 for all buffer
autocmd BufEnter * call ncm2#enable_for_buffer()

" note that must keep noinsert in completeopt, the others is optional
set completeopt=noinsert,menuone,noselect
```

## Usage

By default, look.vim will be disabled. After all, if you're writing code you
don't want the completion popup jumping at you everytime you type something
that remotely looks like a word.

#### To enable it globally

Put this in your `.vimrc`

```vim
let g:ncm2_look_enabled = 1
```

#### To enable it on a per-buffer basis

```vim
:let b:ncm2_look_enabled = 1
```

#### To enable it on a per-filetype basis

Let's say you want to enable it for markdown files.

-   Create a file in `~/.vim/ftplugin/markdown.vim`
-   Put `let b:ncm2_look_enabled = 1` on the file
-   Save and open a markdown file

#### Configuration

###### `ncm2_look_enabled`

_Possible values:_ 0 (default), 1

_Scopes:_ global (`g:ncm2_look_enabled`), buffer (`b:ncm2_look_enabled`)

This option enables the look completion either globally or for the current
buffer.

###### `ncm2_look_use_spell`

_Possible values:_ 0 (default), 1

_Scopes:_ global (`g:ncm2_look_use_spell`)

If this option is enabled, use `&spellfile` as complimentary sources for word
completion. See `:h spellfile` for more details on how that works

###### `ncm2_look_mark`

_Possible values:_ Any valid string (default: look)

_Scopes:_ global (`g:ncm2_look_mark`)

Change the mark used in the completion menu. Default is `look`, as you can see
on the first gif, but any UTF-8 string is valid. For example:

```vim
let g:ncm2_look_mark = '👀'
```

Will result in this:

![mark](https://user-images.githubusercontent.com/48519/44112766-6d1470c0-9fdc-11e8-8a03-146b255222de.gif)

---

**look.vim** © 2018+, Filipe Kiss Released under the [MIT] License.<br>
Authored and maintained by Filipe Kiss.

> GitHub [@filipekiss](https://github.com/filipekiss) &nbsp;&middot;&nbsp;
> Twitter [@filipekiss](https://twitter.com/filipekiss)

[mit]: LICENSE.md
[neco-look]: https://github.com/ujihisa/neco-look
[ncm2]: https://github.com/ncm2/ncm2
[nvim-yarp]: https://github.com/roxma/nvim-yarp
[vim-plug]: https://github.com/junegunn/vim-plug
