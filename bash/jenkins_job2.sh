#step1 xmr

DATE=$( date "+%Y%m%d%H%M")
NAME="${JOB_NAME}_${MODE}_${DATE}_${BUILD_NUMBER}"
PROJ="xmr-debian"
tar -cvf ${NAME}.tar ${WORKSPACE}/scripts/
tar -rvf ${NAME}.tar ${WORKSPACE}/solution/
cp ${NAME}.tar ${WORKSPACE}/${PROJ}/usr/src/${PROJ}/xm.tar
echo "Build № ${NAME} is Good!"

#step2 xmr
DATE=$(date "+%Y-%m-%d")
NAME="${JOB_NAME}_${MODE}_${DATE}_${BUILD_NUMBER}"
rm -f *.deb
#gzip --best -n /opt/xmr-debian/usr/share/doc/xmr-debian/changelog.Debian
PROJ="xmr-debian"
echo "Name of deb-package = ${PROJ}"

debproj=${WORKSPACE}/${PROJ}
echo "Project Directory = ${debproj}"

debfile=${WORKSPACE}/${PROJ}.deb
echo "Package Deb File = ${debfile}"

pif=$debproj/DEBIAN/postinst
echo "PostInstall File = ${pif}"

dstfile=/var/www/html/${PROJ}_${DATE}_amd64.deb
echo "Destination File = ${dstfile}"

if [ -f "$debfile" ]; then
  echo "File deb: ${debfile} exist, need remove it"
  sudo rm -f $debfile
  echo "File deb: ${debfile} removed"
fi
chmod -R 644 $debproj
chmod 755 $pif
chown -R root:root $debproj
dpkg-deb --build $debproj

if [ -f "${WORKSPACE}/xmr-debian.deb" ]; then
  echo "Check deb-package ${WORKSPACE}/xmr-debian.deb"
  lintian $WORKSPACE/${PROJ}.deb
  cp $debfile ${dstfile}
  mv $debfile ${PROJ}_${DATE}_amd64.deb
else
  echo "File deb: ${debfile} not exist"
fi

#rsync -a --exclude=${EXCLUDE} ${ROOTPATH}/{$$same}/ ${TUDA}/${PRJNAME}
