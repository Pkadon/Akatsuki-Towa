label avg29040(trans=fade_in):

$ play_music("ED6104.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "bcv_oc001_win_02.ogg"
get_char('c13') '[convertstrid(1100021)]' (**arg(1, 1100021))
return "avg29040"