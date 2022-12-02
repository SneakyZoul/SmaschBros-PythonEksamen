import os
import pandas as pd
from config.definitions import ROOT_DIR

data = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'data.csv'))


def fetching_data():
    datas = pd.DataFrame(data)  # laver et nyt DataFrame ud fra de "navne" du gere vil have
    df = datas.dropna()
    return df


def fetching_images():
    paths = [
        os.path.join(ROOT_DIR, 'data/img', 'mario.png'),
        os.path.join(ROOT_DIR, 'data/img', 'donkeykong.png'),
        os.path.join(ROOT_DIR, 'data/img', 'link.png'),
        os.path.join(ROOT_DIR, 'data/img', 'samus.png'),
        os.path.join(ROOT_DIR, 'data/img', 'yoshi.png'),
        os.path.join(ROOT_DIR, 'data/img', 'kirby.png'),
        os.path.join(ROOT_DIR, 'data/img', 'fox.png'),
        os.path.join(ROOT_DIR, 'data/img', 'pikachu.png'),
        os.path.join(ROOT_DIR, 'data/img', 'darksamus.png'),
        os.path.join(ROOT_DIR, 'data/img', 'luigi.png'),
        os.path.join(ROOT_DIR, 'data/img', 'ness.png'),
        os.path.join(ROOT_DIR, 'data/img', 'captainfalcon.png'),
        os.path.join(ROOT_DIR, 'data/img', 'jigglypuff.png'),
        os.path.join(ROOT_DIR, 'data/img', 'peach.png'),
        os.path.join(ROOT_DIR, 'data/img', 'daisy.png'),
        os.path.join(ROOT_DIR, 'data/img', 'bowser.png'),
        os.path.join(ROOT_DIR, 'data/img', 'iceclimbers.png'),
        os.path.join(ROOT_DIR, 'data/img', 'sheik.png'),
        os.path.join(ROOT_DIR, 'data/img', 'zelda.png'),
        os.path.join(ROOT_DIR, 'data/img', 'drmario.png'),
        os.path.join(ROOT_DIR, 'data/img', 'pichu.png'),
        os.path.join(ROOT_DIR, 'data/img', 'falco.png'),
        os.path.join(ROOT_DIR, 'data/img', 'marth.png'),
        os.path.join(ROOT_DIR, 'data/img', 'lucina.png'),
        os.path.join(ROOT_DIR, 'data/img', 'younglink.png'),
        os.path.join(ROOT_DIR, 'data/img', 'ganondorf.png'),
        os.path.join(ROOT_DIR, 'data/img', 'mewtwo.png'),
        os.path.join(ROOT_DIR, 'data/img', 'roy.png'),
        os.path.join(ROOT_DIR, 'data/img', 'chrom.png'),
        os.path.join(ROOT_DIR, 'data/img', 'mrgamewatch.png'),
        os.path.join(ROOT_DIR, 'data/img', 'metaknight.png'),
        os.path.join(ROOT_DIR, 'data/img', 'pit.png'),
        os.path.join(ROOT_DIR, 'data/img', 'darkpit.png'),
        os.path.join(ROOT_DIR, 'data/img', 'zerosuitsamus.png'),
        os.path.join(ROOT_DIR, 'data/img', 'wario.png'),
        os.path.join(ROOT_DIR, 'data/img', 'snake.png'),
        os.path.join(ROOT_DIR, 'data/img', 'ike.png'),
        os.path.join(ROOT_DIR, 'data/img', 'pokemontrainer.png'),
        os.path.join(ROOT_DIR, 'data/img', 'diddykong.png'),
        os.path.join(ROOT_DIR, 'data/img', 'lucas.png'),
        os.path.join(ROOT_DIR, 'data/img', 'sonic.png'),
        os.path.join(ROOT_DIR, 'data/img', 'kingdedede.png'),
        os.path.join(ROOT_DIR, 'data/img', 'olimar.png'),
        os.path.join(ROOT_DIR, 'data/img', 'lucario.png'),
        os.path.join(ROOT_DIR, 'data/img', 'rob.png'),
        os.path.join(ROOT_DIR, 'data/img', 'toonlink.png'),
        os.path.join(ROOT_DIR, 'data/img', 'wolf.png'),
        os.path.join(ROOT_DIR, 'data/img', 'villager.png'),
        os.path.join(ROOT_DIR, 'data/img', 'megaman.png'),
        os.path.join(ROOT_DIR, 'data/img', 'wiifit.png'),
        os.path.join(ROOT_DIR, 'data/img', 'rosalina.png'),
        os.path.join(ROOT_DIR, 'data/img', 'littlemac.png'),
        os.path.join(ROOT_DIR, 'data/img', 'greninja.png'),
        os.path.join(ROOT_DIR, 'data/img', 'miibrawler.png'),
        os.path.join(ROOT_DIR, 'data/img', 'miisword.png'),
        os.path.join(ROOT_DIR, 'data/img', 'miigunner.png'),
        os.path.join(ROOT_DIR, 'data/img', 'palutena.png'),
        os.path.join(ROOT_DIR, 'data/img', 'pacman.png'),
        os.path.join(ROOT_DIR, 'data/img', 'robin.png'),
        os.path.join(ROOT_DIR, 'data/img', 'shulk.png'),
        os.path.join(ROOT_DIR, 'data/img', 'bowserjr.png'),
        os.path.join(ROOT_DIR, 'data/img', 'duckhunt.png'),
        os.path.join(ROOT_DIR, 'data/img', 'ryu.png'),
        os.path.join(ROOT_DIR, 'data/img', 'ken.png'),
        os.path.join(ROOT_DIR, 'data/img', 'cloud.png'),
        os.path.join(ROOT_DIR, 'data/img', 'corrin.png'),
        os.path.join(ROOT_DIR, 'data/img', 'bayonetta.png'),
        os.path.join(ROOT_DIR, 'data/img', 'inkling.png'),
        os.path.join(ROOT_DIR, 'data/img', 'ridley.png'),
        os.path.join(ROOT_DIR, 'data/img', 'simon.png'),
        os.path.join(ROOT_DIR, 'data/img', 'richter.png'),
        os.path.join(ROOT_DIR, 'data/img', 'kingkrool.png'),
        os.path.join(ROOT_DIR, 'data/img', 'isabelle.png'),
        os.path.join(ROOT_DIR, 'data/img', 'incineroar.png'),
        os.path.join(ROOT_DIR, 'data/img', 'piranha.png'),
        os.path.join(ROOT_DIR, 'data/img', 'joker.png'),
        os.path.join(ROOT_DIR, 'data/img', 'hero.png'),
        os.path.join(ROOT_DIR, 'data/img', 'banjokazooie.png'),
        os.path.join(ROOT_DIR, 'data/img', 'terry.png'),
        os.path.join(ROOT_DIR, 'data/img', 'byleth.png'),
        os.path.join(ROOT_DIR, 'data/img', 'minmin.png'),
        os.path.join(ROOT_DIR, 'data/img', 'steve.png'),
        os.path.join(ROOT_DIR, 'data/img', 'sephiroth.png'),
        os.path.join(ROOT_DIR, 'data/img', 'pyra.png'),
        os.path.join(ROOT_DIR, 'data/img', 'kazuya.png'),
        os.path.join(ROOT_DIR, 'data/img', 'sora.png')]
    return paths


if __name__ == '__main__':
    print(fetching_data())
