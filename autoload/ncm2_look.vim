if get(s:, 'loaded', 0)
    finish
endif
let s:loaded = 1

let g:ncm2_look#proc = yarp#py3('ncm2_look')

let g:ncm2_look#source = get(g:, 'ncm2_look#look_source', {
            \ 'name': 'buflook',
            \ 'priority': 6,
            \ 'mark': 'look',
            \ 'on_complete': 'ncm2_look#on_complete',
            \ 'on_warmup' : 'ncm2_look#on_warmup'
            \ })

let g:ncm2_look#source = extend(g:ncm2_look#source,
            \ get(g:, 'ncm2_look#source_override', {}),
            \ 'force')

function! ncm2_look#init()
    call ncm2#register_source(g:ncm2_look#source)
endfunction

function! ncm2_look#on_warmup(ctx)
    call g:ncm2_look#proc.jobstart()
endfunction

function! ncm2_look#on_complete(ctx)
    call g:ncm2_look#proc.try_notify('on_complete', a:ctx)
endfunction
