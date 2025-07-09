label avg22201:
stop music

play music "ed7150.ogg"
scene avg_bg_013
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
c11 '[textdict[1128572]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1128573]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c5631 '[textdict[1128574]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1128575]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1128576]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c5621 '[textdict[1128577]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c5621 '[textdict[1128580]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1128581]]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 5)
c23 '[textdict[1128582]]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
c5631 '[textdict[1128583]]'
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li12.ogg"
c43 '[textdict[1128584]]'
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1128585]]'
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128586]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
c5623 '[textdict[1128587]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
c5623 '[textdict[1128588]]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1128589]]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch03_b.ogg"
c23 '[textdict[1128590]]'
return