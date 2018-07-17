command! LookDisable       let g:ncm2_look_enabled = 0
command! LookEnable        let g:ncm2_look_enabled = 1
command! LookDisableBuffer let b:ncm2_look_enabled = 0
command! LookEnableBuffer  let b:ncm2_look_enabled = 1
command! LookToggle call ncm2_look#toggle('global')
command! LookToggleBuffer call ncm2_look#toggle('buffer')
