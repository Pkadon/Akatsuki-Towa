label avg12476(trans=fade_in):

$ play_music("ED6516.ogg")
scene placeholderbackground
$ update_narrator('c61')
$ update_portrait('oc006_01 3', 'p6', [l(-5), light, flip], 6)
window show
with trans
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144061)]' (**arg(1, 1144061))
$ update_portrait('oc006_01 3', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144062)]' (**arg(2, 1144062))
hide p6
get_char('c0') '[convertstrid(1144063)]' (**arg(3, 1144063))
$ update_portrait('uc003_04 3', 'p1045', [r(-14), r_shake, light], 6)
get_char('c10453') '[convertstrid(1144064)]' (**arg(4, 1144064))
hide p1045
get_char('c0') '[convertstrid(1144065)]' (**arg(5, 1144065))
$ update_portrait('uc003_04 4', 'p1124', [r(-14), light], 6)
get_char('c11243') '[convertstrid(1144066)]' (**arg(6, 1144066))
hide p1124
$ update_portrait('uc003_04 3', 'p1045', [r(-14), r_shake, light], 6)
get_char('c10453') '[convertstrid(1144067)]' (**arg(7, 1144067))
hide p1045
$ update_portrait('uc003_04 4', 'p1124', [r(-14), light], 6)
get_char('c11243') '[convertstrid(1144068)]' (**arg(8, 1144068))
$ update_portrait('uc003_04 4', 'p1124', [r(-14), dark], 5)
get_char('c11671') '[convertstrid(1144069)]' (**arg(9, 1144069))
$ update_portrait('uc003_04 4', 'p1124', [r(-14), light], 6)
get_char('c11243') '[convertstrid(1144070)]' (**arg(10, 1144070))
$ update_portrait('uc003_04 4', 'p1124', [r(-14), dark], 5)
get_char('c11671') '[convertstrid(1144071)]' (**arg(11, 1144071))
get_char('c11671') '[convertstrid(1144072)]' (**arg(12, 1144072))
get_char('c11671') '[convertstrid(1144073)]' (**arg(13, 1144073))
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144074)]' (**arg(14, 1144074))
hide p1124
$ update_portrait('oc006_01 3', 'p6', [l(-5), dark, flip], 5)
get_char('c11673') '[convertstrid(1144075)]' (**arg(15, 1144075))
get_char('c11673') '[convertstrid(1144076)]' (**arg(16, 1144076))
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144077)]' (**arg(17, 1144077))
$ update_portrait('oc006_01 3', 'p6', [l(-5), dark, flip], 5)
get_char('c11673') '[convertstrid(1144078)]' (**arg(18, 1144078))
$ update_portrait('oc006_01 3', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144079)]' (**arg(19, 1144079))
return "avg12476"