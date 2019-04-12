project('2048', 'cpp',
  default_options : ['cpp_std=c++14'])

main_target_name = '2048'

subdir('src')
hdrs = include_directories('src/headers')

executable(main_target_name, sources,
  include_directories : hdrs,
  install : true)

install_data(['data/scores.txt', 'data/statistics.txt'],
  install_dir : 'data')
