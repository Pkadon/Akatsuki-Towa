label avg25050:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 2', 'p2003', [mid(-2), light], 6)
$ update_narrator('c20033')
window show
with fade_in
play sfx2 "other_7021.ogg"
c20033 '[convertstrid(1210131)]'
hide p2003
$ update_portrait('uc001_02 1', 'p2002', [mid(6), light], 6)
c20023 '[convertstrid(1210132)]'
hide p2002
$ update_portrait('uc001_01 2', 'p2003', [mid(-2), light], 6)
c20033 '[convertstrid(1210133)]'
hide p2003
$ update_portrait('uc001_02 1', 'p2002', [mid(6), light], 6)
c20023 '[convertstrid(1210134)]'
hide p2002
$ update_portrait('uc001_01 1', 'p2003', [mid(-2), light], 6)
c20033 '[convertstrid(1210135)]'
$ update_portrait('uc001_01 1', 'p2003', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
c20033 '[convertstrid(1210136)]'
hide p2003
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210137)]'
hide p1
$ update_portrait('uc001_02 2', 'p2002', [mid(6), light], 6)
c20023 '[convertstrid(1210138)]'
hide p2002
$ update_portrait('uc001_01 1', 'p2003', [mid(-2), light], 6)
play sfx2 "other_7085.ogg"
c20033 '[convertstrid(1210139)]'
return