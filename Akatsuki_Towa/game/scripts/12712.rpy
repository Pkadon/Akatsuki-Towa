label avg12712:

$ play_music("ed7151.ogg")
scene avg_bg_049
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1170731)]' (**arg(1, 1170731))
get_char('c0') '[convertstrid(1170732)]' (**arg(2, 1170732))
$ update_portrait('uc002_03 1', 'p530', [l_entrance(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1170733)]' (**arg(3, 1170733))
hide p530
$ update_portrait('uc002_03 1', 'p531', [l(-23), light, flip], 6)
get_char('c5311') '[convertstrid(1170734)]' (**arg(4, 1170734))
$ update_portrait('uc002_03 1', 'p531', [l(-23), dark, flip], 5)
get_char('c14183') '[convertstrid(1170735)]' (**arg(5, 1170735))
get_char('c14193') '[convertstrid(1170736)]' (**arg(6, 1170736))
get_char('c14183') '[convertstrid(1170737)]' (**arg(7, 1170737))
$ update_portrait('uc002_03 1', 'p531', [l(-23), light, flip], 6)
get_char('c5311') '[convertstrid(1170738)]' (**arg(8, 1170738))
hide p531
$ update_portrait('uc002_03 2', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1170739)]' (**arg(9, 1170739))
$ update_portrait('uc002_03 1', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1170740)]' (**arg(10, 1170740))
$ update_portrait('uc002_03 1', 'p530', [l(-23), dark, flip], 5)
get_char('c14183') '[convertstrid(1170741)]' (**arg(11, 1170741))
hide p530
$ update_portrait('uc002_03 1', 'p531', [l_midback(-23), light, flip], 6)
play sfx2 "other_7007.ogg"
get_char('c5311') '[convertstrid(1170742)]' (**arg(12, 1170742))
$ update_portrait('uc002_03 1', 'p531', [l(-23), dark, flip], 5)
get_char('c14193') '[convertstrid(1170743)]' (**arg(13, 1170743))
hide p531
$ update_portrait('uc002_03 1', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1170744)]' (**arg(14, 1170744))
$ play_music("ed7511.ogg")
$ update_portrait('uc002_03 1', 'p530', [l(-23), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1170745)]' (**arg(15, 1170745)) with shake
hide p530
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('uc002_03 1', 'p531', [l(-23), light, flip], 6)
get_char('c5311') '[convertstrid(1170746)]' (**arg(16, 1170746))
hide p531
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1170747)]' (**arg(17, 1170747))
$ update_portrait('st061_01 1', 'p1304', [l(-2), l_shake, light, flip], 6)
get_char('c13041') '[convertstrid(1170748)]' (**arg(18, 1170748))
hide p1304
$ update_portrait('uc002_03 1', 'p530', [l(-23), light, flip], 6)
get_char('c5301') '[convertstrid(1170749)]' (**arg(19, 1170749))
hide p530
$ update_portrait('uc002_03 1', 'p531', [l(-23), light, flip], 6)
get_char('c5311') '[convertstrid(1170750)]' (**arg(20, 1170750))
$ update_portrait('uc002_03 1', 'p531', [l(-23), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1170751)]' (**arg(21, 1170751))
return