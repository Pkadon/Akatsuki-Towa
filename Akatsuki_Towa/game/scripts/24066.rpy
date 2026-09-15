label avg24066(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200264)]' (**arg(1, 1200264))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7573') '[convertstrid(1200265)]' (**arg(2, 1200265))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200266)]' (**arg(3, 1200266))
return "avg24066"