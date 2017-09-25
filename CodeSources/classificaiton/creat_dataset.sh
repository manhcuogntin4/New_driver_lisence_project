#!/bin/bash
DATA_ROOT="DATASET"
mkdir $DATA_ROOT/resized
mkdir $DATA_ROOT/resized/merge
for dir in cartegrise cni passeport permis nouveaupermis;
  do
    echo Resize of directory: $dir ;
    case ${dir:0:2} in
      cn)
        CLASS=1
        ;;
      ca)
        CLASS=2
        ;;
      pa)
        CLASS=3
        ;;
      pe)
        CLASS=4
        ;;
      no)
		CLASS=5
		;;
      *)
        echo "Not found"
        exit 1
    esac
    echo Classe : $CLASS ;
    for i in $DATA_ROOT/$dir/*;
      do
        echo $dir/`basename "$i"`,$CLASS,0,0,0,0,0,0 >> $DATA_ROOT/$dir.csv ;
      done
    ./bin/extractRect $DATA_ROOT/$dir.csv --resize_width=224 --full_image --noise_rotation=180 --samples 5 $DATA_ROOT/resized/$dir ;
    cat $DATA_ROOT/resized/$dir/results.csv >> $DATA_ROOT/resized/merge/results.csv
  done
mkdir $DATA_ROOT/resized/merge/1
mkdir $DATA_ROOT/resized/merge/2
mkdir $DATA_ROOT/resized/merge/3
mkdir $DATA_ROOT/resized/merge/4
mkdir $DATA_ROOT/resized/merge/5
cp $DATA_ROOT/resized/cni/1/* $DATA_ROOT/resized/merge/1/
cp $DATA_ROOT/resized/ca*/2/* $DATA_ROOT/resized/merge/2/
cp $DATA_ROOT/resized/pa*/3/* $DATA_ROOT/resized/merge/3/
cp $DATA_ROOT/resized/pe*/4/* $DATA_ROOT/resized/merge/4/
cp $DATA_ROOT/resized/no*/5/* $DATA_ROOT/resized/merge/5/
ln -s $DATA_ROOT/resized/merge results/resized