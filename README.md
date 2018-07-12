# ncm2-look.vim

Port of the [neco-look] plugin for [NCM2]

Using `look` to complete words in english

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
don't want the completion popup jumping at you everytime you type something that
remotely looks like a word.

#### To enable it globally

Put this in your `.vimrc`

```vim
let g:ncm2_look_enabled = 1
```

#### To enable it on a per-buffer basis

```vim
:let b:ncm2_look_enabled = 1
```

#### To enable it on a pre-filetype basis

Let's say you want to enable it for markdown files.

-   Create a file in `~/.vim/ftplugin/markdown.vim`
-   Put `let b:ncm2_look_enabled = 1` on the file
-   Save and open a markdown file

[neco-look]: https://github.com/ujihisa/neco-look
[ncm2]: https://github.com/ncm2/ncm2
[nvim-yarp]: https://github.com/roxma/nvim-yarp
[vim-plug]: https://github.com/junegunn/vim-plug
