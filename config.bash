#checking for: opencvge3.0.0
opencv_version=`pkg-config --modversion opencv`
if [ "$(perl -e '($x,$y)=@ARGV; print $x ge $y' opencv_version 3.0.0)" != "1" ]
then
	echo "FATAL: opencv not found"
fi
#checking for: libgutge7.0
libgut_version=`pkg-config --modversion libgut`
if [ "$(perl -e '($x,$y)=@ARGV; print $x ge $y' libgut_version 7.0)" != "1" ]
then
	echo "FATAL: libgut not found"
fi
