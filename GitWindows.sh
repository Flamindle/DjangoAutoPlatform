#!/bin/zsh

UserName=`whoami`

# 首字母大写
a=`echo ${UserName:0:1} | tr "[:lower:]" "[:upper:]"`
b=`echo ${UserName:1}`
EngName=$a$b

# 绝对路径：任意位置打开
# 当前文件的目录路径，比如/Users/flamindle/Desktop/MacBookAirM2
path=$(dirname "$0")
# 当前文件的名字，比如GitMacOS.command
name=$(basename "$0")
# 当前文件的绝对路径，比如/Users/flamindle/Desktop/MacBookAirM2/GitMacOS.command
path_name="$path/$name"

# 查看当前脚本的源代码你
# more $path_name

# 定义颜色变量
BLACK='\033[0;30m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
# 定义文字风格变量
BOLD='\033[1m'
UNDERLINE='\033[4m'
REVERSED='\033[7m'
ITALIC='\033[3m'
RESET='\033[0m'  # 重置颜色和样式


timestampall=`date +"_%y%m%d_%H%M%S"`

turn_back(){
	echo "\n是否继续?\n"
  echo "[1: 是]"
  echo "[0: 否]\n"
  read YN
	#FUNCNAME[0]：当前正在执行的函数名
	#FUNCNAME[1]：调用它的上一级函数
	#FUNCNAME[2]：再往上的函数 ……
  if [ "$YN" -eq 1 ] ; then
    ${FUNCNAME[1]}
  fi

  if [ "$YN" -eq 0 ] ; then
    $path_name
  fi
  exit 0
}

goodbye(){
    echo "\n别之期期，子子安好！拜，$EngName，\n纵使代码千百行，不及我送王伦情:)"
    sleep 1
    exit
}


git_add_commit_push(){
	cd $path
	git add .
	echo "请输入新版本的更改内容，点击回车键开始："
	read -e git_commit_msg
	git commit -m "$git_commit_msg"
	echo "正在推送到 GitHub，请稍候..."
	git push
	echo "✅ 推送完成！"
	# 停留
	turn_back
}

git_clone(){
	echo "请输入项目的地址："
	read url_git
	git clone $url_git
	echo "✅ Clone完成！"
	# 停留
	turn_back
}


git_pull(){
	cd $path
	git pull
}

git_all_repro(){
	cd $path
	#一旦脚本中某个命令返回非 0 状态（报错），整个脚本会立刻退出。
	set -e
	echo "请输入评论："
	read all_comment
	repos=(
	  "."
	  "./Rog16"
	  "./Rog16/Flask_aerotai.cn"
	  "./Rog16/www.aerotai.cn"
	  "./Rog16/www.aerotai"
	)

	for repo in "${repos[@]}"; do
	  if [ ! -d "$repo/.git" ]; then
	    echo "⚠️  Skip $repo (not a git repo or folder not exist)"
	    continue
	  fi

	  echo "🚀 Pushing $repo ..."
	  cd "$repo"
	  git add .
	  git commit -m "$all_comment" || true   # 没有改动时不报错
	  git push
	  cd - > /dev/null
	done

	echo "✅ 所有项目已经推送成功!"
	$path_name
}


#************************************************************************************************

command_to_sh(){
	cd $path
	# 把 GitMacOS.command 复制到当前路径并改名为 GitMacOS.sh
	# 如果目标已存在则覆盖
	src="GitMacOS.command"
	dst="GitWindows.sh"

	if [ -f "$src" ]; then
	    cp -f "$src" "$dst"
	    echo "✅ 已复制并覆盖为: $dst"
	else
	    echo "❌ 未找到 $src 文件"
	fi
	chmod +x GitWindows.sh
	$path_name
}

sh_to_command(){
	cd $path
	# 把 GitWindows.sh 复制到当前路径并改名为 GitMacOS.command
	# 如果目标已存在则覆盖
	src="GitWindows.sh"
	dst="GitMacOS.command"

	if [ -f "$src" ]; then
	    cp -f "$src" "$dst"
	    echo "✅ 已复制并覆盖为: $dst"
	else
	    echo "❌ 未找到 $src 文件"
	fi
	chmod +x GitMacOS.command
	sleep 3
	$path_name
}


sync_files(){
	cd "$path" || exit
	# 遇错退出
	set -e

	repos=(
	  "."
	  "./Rog16"
	  "./Rog16/Flask_aerotai.cn"
	  "./Rog16/www.aerotai.cn"
	  "./Rog16/www.aerotai"
	)

	for repo in "${repos[@]}"; do
	  if [ ! -d "$repo/.git" ]; then
	    echo "⚠️  Skip $repo (not a git repo or folder not exist)"
	    continue
	  fi

	  echo "🚀 同步中…… $repo ..."
	  src1="GitMacOS.command"
	  src2="GitWindows.sh"
	  # 文件复制，失败也不影响下一个仓库
	  cp -f "$src1" "$repo/" || true
	  cp -f "$src2" "$repo/" || true
	done

	# 返回上一次目录
	cd - > /dev/null

	echo "✅ 所有项目文件已同步完成!"
	sleep 3
	$path_name

}


ui_windows(){
	echo "\nGit自动化脚本\n"
	echo "=========Git篇=========          =========文件篇========="

	echo "  1. Clone到本地*                     11. command同步到sh"
	echo "  2. Push到Github                     12. sh同步到command"
	echo "  3. Pull到本地*                      13. 同步该文件"
	echo "  4. 初始化*"
	echo "  5. 一键git push所有项目"
	echo "  6. 初始化*"

	echo "\n适于愿兮,恰与君逢！$EngName, 你好! \n请依上文，按序而选:\n[0] 退出\n"

	read IndexID

	if [ "$IndexID" -eq 0 ] ; then
    goodbye
	fi

	if [ "$IndexID" -eq 2 ]; then
		git_add_commit_push
	fi

	if [ "$IndexID" -eq 3 ]; then
		git_pull
	fi

	if [ "$IndexID" -eq 5 ]; then
		git_all_repro
	fi

	if [ "$IndexID" -eq 6 ]; then
		sleep 3
	fi
	if [ "$IndexID" -eq 7 ]; then
		sleep 3
	fi
	if [ "$IndexID" -eq 8 ]; then
		sleep 3
	fi
	if [ "$IndexID" -eq 9 ]; then
		sleep 3
	fi
	if [ "$IndexID" -eq 10 ]; then
		sleep 3
	fi

	if [ "$IndexID" -eq 11 ]; then
		command_to_sh
	fi

	if [ "$IndexID" -eq 12 ]; then
		sh_to_command
	fi

	if [ "$IndexID" -eq 13 ]; then
		sync_files
	fi
}

ui_windows
