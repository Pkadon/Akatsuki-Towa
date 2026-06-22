label avg29004:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1216020)]' (**arg(1, 1216020))
get_char('c0') '[convertstrid(1216021)]' (**arg(2, 1216021))
get_char('c0') '[convertstrid(1216022)]' (**arg(3, 1216022))
get_char('c0') '[convertstrid(1216023)]' (**arg(4, 1216023))
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 6)
get_char('c2093') '[convertstrid(1216024)]' (**arg(5, 1216024))
hide p209
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216025)]' (**arg(6, 1216025))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216026)]' (**arg(7, 1216026))
hide p1
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 6)
get_char('c2093') '[convertstrid(1216027)]' (**arg(8, 1216027))
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 6)
get_char('c2093') '[convertstrid(1216028)]' (**arg(9, 1216028))
menu:
    extend ""
    '[convertstrid(1216029)]':
        call avg29005
    '[convertstrid(1216030)]':
        call avg29006
return