label avg12153(trans=fade_in):

$ play_music("ED6107.ogg")
scene avg_bg_038
$ update_narrator('c9621')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c9621') '[convertstrid(1128380)]' (**arg(1, 1128380))
return "avg12153"