project('2048', 'cpp',
  default_options : ['cpp_std=c++14', 'warning_level=1', 'buildtype=release'])

main_target_name = '2048'
sources = files('src/2048.cpp', 'src/gameboard.cpp', 'src/game.cpp', 'src/game-input.cpp', 'src/game-graphics.cpp', 'src/game-pregamemenu.cpp', 'src/global.cpp', 'src/loadresource.cpp', 'src/menu.cpp', 'src/saveresource.cpp', 'src/scores.cpp', 'src/statistics.cpp', 'src/tile.cpp')
hdrs = include_directories('src/headers')

cpp2048_exe = executable(main_target_name, sources, 
  include_directories : hdrs,
  install : true)

python = find_program('python')
test('2048startup', python,
  args: ['src/run_stdin.py', cpp2048_exe, '4'],
  workdir: meson.source_root())

install_data(['data/scores.txt', 'data/statistics.txt'],
  install_dir : 'data')

