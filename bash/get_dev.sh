#! /bin/bash
if [[ -f "/srv/install/md5sum.txt" && -s "/srv/install/md5sum.txt" ]]; then
  rm -rfv /srv/install/*
    echo "rm -rf /srv/install/*"
fi

## unpack for install

wget -P /srv/scripts http://${IP}/${env}.iso
umount /mnt
mount -o loop -t iso9660 /srv/scripts/${env}.iso /mnt
cp -rf /mnt/* /srv/install/
rm -vf /home/storages/install/iso/${env}.iso
mv -vf /srv/scripts/${env}.iso /home/storages/install/iso/${env}.iso
chmod -R 755 /srv/install/
umount /mnt

## crutch for aptly

if [[ -f "/srv/install/md5sum.txt" && -s "/srv/install/md5sum.txt" ]]; then
    cd /srv/install/
    find . -name "*\%3a*.deb" -exec bash -c 'cp $1 ${1//\%3a/\:}' _ {} \;
    echo "rename %3"
    ls -la /srv/install/
fi

## end