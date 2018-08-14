if get(s:, 'loaded', 0)
    finish
endif
let s:loaded = 1

let g:ncm2_look_enabled = get(g:, 'ncm2_look_enabled',  0)

let g:ncm2_look_use_spell = get(g:, 'ncm2_look_use_spell',  0)

let g:ncm2_look#proc = yarp#py3('ncm2_look')

let g:ncm2_look#source = get(g:, 'ncm2_look#look_source', {
            \ 'name': 'buflook',
            \ 'priority': 6,
            \ 'mark': 'look',
            \ 'on_complete': 'ncm2_look#on_complete',
            \ 'on_warmup': 'ncm2_look#on_warmup'
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
    let s:is_enabled = get(b:, 'ncm2_look_enabled',
                \ get(g:, 'ncm2_look_enabled', 0))
    if ! s:is_enabled
        return
    endif
    call g:ncm2_look#proc.try_notify('on_complete', a:ctx)
endfunction


function! ncm2_look#toggle(scope)
    let s:ncm2_look = {}
    let s:ncm2_look['global'] = get(g:, 'ncm2_look_enabled', 0)
    let s:ncm2_look['buffer'] = get(b:, 'ncm2_look_enabled', s:ncm2_look['global'])
    if (s:ncm2_look[a:scope] == 1)
        let s:ncm2_look[a:scope]=0
    else
        let s:ncm2_look[a:scope]=1
    endif
    let g:ncm2_look_enabled=s:ncm2_look['global']
    let b:ncm2_look_enabled=s:ncm2_look['buffer']
endfunction
