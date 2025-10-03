label avg1092:

$ play_music("ed7202.ogg")
scene avg_bg_079
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na03_b.ogg"
c13 '[convertstrid(2102004)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 2', 'p59', [l_entrance(-25), light, flip], 6)
c591 '[convertstrid(2102005)]'
$ update_portrait('sc052_01 2', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102006)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
play sfx2 "fight_6019.ogg"
c591 '[convertstrid(2102007)]' (what_size=(gui.text_size*1.3)) with shake
hide p59
hide p1
c0 '[convertstrid(2102008)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102009)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102010)]'
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102011)]'
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102012)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102013)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102014)]'
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102015)]'
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102016)]'
hide p1
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
c6903 '[convertstrid(2102017)]'
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102018)]'
$ update_portrait('sc052_01 5', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102019)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102020)]'
hide p59
hide p1
c0 '[convertstrid(2102021)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102022)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
c5021 '[convertstrid(2102023)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(2102024)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
c5021 '[convertstrid(2102025)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102026)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102027)]'
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(2102028)]'
hide p1
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
c6903 '[convertstrid(2102029)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102030)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l_exit(-25), light, flip], 6)
c591 '[convertstrid(2102031)]'
hide p59
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102032)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102033)]'
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102034)]'
$ update_portrait('oc001_01 23', 'p1', [r(-2), dark], 5)
c5021 '[convertstrid(2102035)]'
$ update_portrait('oc001_01 24', 'p1', [r_exit(-2), light], 6)
c13 '[convertstrid(2102036)]'
hide p1
return