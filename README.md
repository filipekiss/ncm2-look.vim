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

[neco-look]: https://github.com/ujihisa/neco-look
[ncm2]: https://github.com/ncm2/ncm2
[nvim-yarp]: https://github.com/roxma/nvim-yarp
[vim-plug]: https://github.com/junegunn/vim-plug
