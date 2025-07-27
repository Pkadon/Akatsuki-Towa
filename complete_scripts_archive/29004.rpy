label avg29004:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1216020)]'
c0 '[convertstrid(1216021)]'
c0 '[convertstrid(1216022)]'
c0 '[convertstrid(1216023)]'
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[convertstrid(1216024)]'
hide p209
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1216025)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1216026)]'
hide p1
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[convertstrid(1216027)]'
$ update_portrait('st009_01 1', 'p209', [mid(-22), light], 5)
c2093 '[convertstrid(1216028)]'
menu:
    extend ""
    "[textdict[1216029]]":
        call avg29005
    "[textdict[1216030]]":
        call avg29006
return