"""Build a clean public artifact without templates, previews or internal material."""
from pathlib import Path
import argparse
import shutil

SOURCE = Path(__file__).resolve().parents[1]


def prepare(destination):
    # Refuse reuse so stale files cannot silently survive an earlier build.
    destination.mkdir(parents=True, exist_ok=False)
    for name in ['index.html', 'labs.html', 'checklist-convencao.html', '404.html', 'CNAME', 'robots.txt',
                 'sitemap.xml', 'llms.txt', 'llms-full.txt', 'favicon.ico',
                 'favicon.png', 'style.css', 'style-v2.css']:
        shutil.copy2(SOURCE / name, destination / name)
    for name in ['espacos', 'insights', 'servicos', 'en', 'sobre-nos', 'portfolio']:
        shutil.copytree(SOURCE / name, destination / name)
    # Brand manuals and commercial documents are internal material. The only
    # PDF intentionally published is the lead magnet in assets/downloads.
    media_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.avif', '.svg', '.gif',
                        '.ico', '.woff', '.woff2', '.ttf', '.mp4', '.webm'}
    for asset in (SOURCE / 'assets').rglob('*'):
        is_download_pdf = asset.suffix.lower() == '.pdf' and asset.parent == SOURCE / 'assets' / 'downloads'
        if asset.is_file() and (asset.suffix.lower() in media_extensions or is_download_pdf):
            target = destination / asset.relative_to(SOURCE)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset, target)
    (destination / 'scripts').mkdir()
    shutil.copy2(SOURCE / 'scripts/site-ui.js', destination / 'scripts/site-ui.js')
    shutil.copy2(SOURCE / 'scripts/analytics.js', destination / 'scripts/analytics.js')
    print(f'Public artifact prepared: {destination}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=SOURCE.parent / '_site_public')
    prepare(parser.parse_args().output)
