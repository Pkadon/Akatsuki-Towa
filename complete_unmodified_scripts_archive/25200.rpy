label avg25200(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('uc001_01 2', 'p2022', [mid(-2), light], 6)
$ update_narrator('c20223')
window show
with trans
get_char('c20223') '[convertstrid(1210676)]' (**arg(1, 1210676))
hide p2022
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210677)]' (**arg(2, 1210677))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210678)]' (**arg(3, 1210678))
hide p2
$ update_portrait('uc001_01 1', 'p2022', [mid(-2), light], 6)
get_char('c20223') '[convertstrid(1210679)]' (**arg(4, 1210679))
hide p2022
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210680)]' (**arg(5, 1210680))
hide p1
$ update_portrait('uc001_01 1', 'p2022', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c20223') '[convertstrid(1210681)]' (**arg(6, 1210681))
return "avg25200"