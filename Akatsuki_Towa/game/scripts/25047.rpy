label avg25047:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2002', [mid(6), light], 6)
$ update_narrator('c20023')
window show
with fade_in
get_char('c20023') '[convertstrid(1210120)]' (**arg(1, 1210120))
hide p2002
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210121)]' (**arg(2, 1210121))
hide p2
$ update_portrait('uc001_02 2', 'p2002', [mid(6), light], 6)
get_char('c20023') '[convertstrid(1210122)]' (**arg(3, 1210122))
menu:
    extend ""
    '[convertstrid(1214999)]':
        call avg25048
    '[convertstrid(1215000)]':
        call avg25000
return