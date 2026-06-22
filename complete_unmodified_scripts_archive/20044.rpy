label avg20044:

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1002537)]' (**arg(1, 1002537))
$ update_portrait('uc003_01 1', 'p581', [l(-26), light, flip], 6)
get_char('c5811') '[convertstrid(1002538)]' (**arg(2, 1002538))
hide p581
$ update_portrait('uc003_01 1', 'p582', [l(-26), light, flip], 6)
get_char('c5821') '[convertstrid(1002539)]' (**arg(3, 1002539))
$ update_portrait('uc003_01 1', 'p582', [l(-26), dark, flip], 5)
get_char('c5863') '[convertstrid(1002540)]' (**arg(4, 1002540))
$ update_portrait('uc003_01 1', 'p582', [l(-26), light, flip], 6)
get_char('c5821') '[convertstrid(1002541)]' (**arg(5, 1002541))
hide p582
$ update_portrait('uc003_01 1', 'p581', [l(-26), light, flip], 6)
play sfx2 "fight_6020.ogg"
get_char('c5811') '[convertstrid(1002542)]' (**arg(6, 1002542))
$ update_portrait('uc003_01 1', 'p581', [l(-26), dark, flip], 5)
$ update_portrait('sc020_01 2', 'p28', [r_entrance(-10), light], 6)
get_char('c283') '[convertstrid(1002543)]' (**arg(7, 1002543))
hide p581
$ update_portrait('sc020_01 2', 'p28', [r(-10), dark], 5)
$ update_portrait('uc003_01 1', 'p583', [l(-26), light, flip], 6)
get_char('c5831') '[convertstrid(1002544)]' (**arg(8, 1002544))
hide p583
$ update_portrait('uc003_01 1', 'p584', [l(-26), light, flip], 6)
get_char('c5841') '[convertstrid(1002545)]' (**arg(9, 1002545))
hide p584
$ update_portrait('uc003_01 1', 'p585', [l(-26), light, flip], 6)
get_char('c5851') '[convertstrid(1002546)]' (**arg(10, 1002546))
$ update_portrait('uc003_01 1', 'p585', [l(-26), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
play sfxvoice "bcv_sc020_sc01_04.ogg"
get_char('c283') '[convertstrid(1002547)]' (**arg(11, 1002547))
$ update_portrait('sc020_01 4', 'p28', [r_midback(-10), light], 6)
play sfx2 "fight_6007.ogg"
play sfxvoice "bcv_sc020_sc01_05.ogg"
get_char('c283') '[convertstrid(1002548)]' (**arg(12, 1002548))
hide p585
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('uc003_01 3', 'p582', [l(-26), l_shake, light, flip], 6)
play sfx2 "fight_6001.ogg"
get_char('c5821') '[convertstrid(1002549)]' (**arg(13, 1002549))
hide p582
$ update_portrait('uc003_01 3', 'p583', [l(-26), light, flip], 6)
get_char('c5831') '[convertstrid(1002550)]' (**arg(14, 1002550))
hide p583
$ update_portrait('uc003_01 3', 'p584', [l(-26), light, flip], 6)
get_char('c5841') '[convertstrid(1002551)]' (**arg(15, 1002551))
$ update_portrait('uc003_01 3', 'p584', [l(-26), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002552)]' (**arg(16, 1002552))
hide p584
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('uc003_01 3', 'p585', [l(-26), light, flip], 6)
get_char('c5851') '[convertstrid(1002553)]' (**arg(17, 1002553))
$ update_portrait('uc003_01 3', 'p585', [l(-26), dark, flip], 5)
$ update_portrait('sc020_01 1', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002554)]' (**arg(18, 1002554))
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002555)]' (**arg(19, 1002555))
hide p585
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
play sfxvoice "avg_vocal_ai07.ogg"
get_char('c5221') '[convertstrid(1002556)]' (**arg(20, 1002556))
$ update_portrait('oc008_01 1', 'p588', [l_entrance(-5), light, flip], 6)
get_char('c5881') '[convertstrid(1002557)]' (**arg(21, 1002557))
$ update_portrait('oc008_01 1', 'p588', [l(-5), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002558)]' (**arg(22, 1002558))
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('oc008_01 5', 'p588', [l(-5), light, flip], 6)
get_char('c5881') '[convertstrid(1002559)]' (**arg(23, 1002559))
hide p588
$ update_portrait('oc008_01 1', 'p589', [l(-5), light, flip], 6)
get_char('c5891') '[convertstrid(1002560)]' (**arg(24, 1002560))
$ update_portrait('oc008_01 5', 'p589', [l(-5), light, flip], 6)
play sfx2 "fight_6021.ogg"
get_char('c5891') '[convertstrid(1002561)]' (**arg(25, 1002561))
$ update_portrait('oc008_01 5', 'p589', [l(-5), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r(-10), r_shake, light], 6)
play sfx2 "fight_6019.ogg"
get_char('c283') '[convertstrid(1002562)]' (**arg(26, 1002562))
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('oc008_01 4', 'p589', [l(-5), light, flip], 6)
get_char('c5891') '[convertstrid(1002563)]' (**arg(27, 1002563))
$ update_portrait('oc008_01 4', 'p589', [l(-5), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002564)]' (**arg(28, 1002564))
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('oc008_01 5', 'p589', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_ai06.ogg"
get_char('c5891') '[convertstrid(1002565)]' (**arg(29, 1002565))
$ update_portrait('oc008_01 1', 'p589', [l(-5), light, flip], 6)
get_char('c5891') '[convertstrid(1002566)]' (**arg(30, 1002566))
$ update_portrait('oc008_01 1', 'p589', [l(-5), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r_midback(-10), light], 6)
play sfx2 "fight_6017.ogg"
get_char('c283') '[convertstrid(1002567)]' (**arg(31, 1002567))
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('oc008_01 1', 'p589', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ai12.ogg"
get_char('c5891') '[convertstrid(1002568)]' (**arg(32, 1002568))
$ update_portrait('oc008_01 1', 'p589', [l(-5), dark, flip], 5)
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002569)]' (**arg(33, 1002569))
$ update_portrait('sc020_01 4', 'p28', [r(-10), dark], 5)
$ update_portrait('oc008_01 5', 'p589', [l(-5), light, flip], 6)
get_char('c5891') '[convertstrid(1002570)]' (**arg(34, 1002570))
$ update_portrait('oc008_01 5', 'p589', [l(-5), dark, flip], 5)
$ update_portrait('sc020_01 2', 'p28', [r(-10), r_shake, light], 6)
get_char('c283') '[convertstrid(1002571)]' (**arg(35, 1002571))
$ update_portrait('sc020_01 2', 'p28', [r(-10), dark], 5)
$ update_portrait('oc008_01 4', 'p589', [l(-5), light, flip], 6)
get_char('c5891') '[convertstrid(1002572)]' (**arg(36, 1002572))
$ update_portrait('oc008_01 5', 'p589', [l_exit(-5), light, flip], 6)
play sfxvoice "avg_vocal_ai06.ogg"
get_char('c5891') '[convertstrid(1002573)]' (**arg(37, 1002573))
hide p589
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002574)]' (**arg(38, 1002574))
$ update_portrait('sc020_01 4', 'p28', [r(-10), light], 6)
get_char('c283') '[convertstrid(1002575)]' (**arg(39, 1002575))
return