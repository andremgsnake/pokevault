import json, pathlib, urllib.request
root=pathlib.Path(__file__).resolve().parent.parent
dist=root/'dist'
(dist/'data').mkdir(parents=True,exist_ok=True)
base='https://downloads.s3.cardmarket.com/productCatalog/'
for name,path,key in [('catalog','productList/products_singles_6.json','products'),('prices','priceGuide/price_guide_6.json','priceGuides')]:
    request=urllib.request.Request(base+path,headers={'User-Agent':'PokeVault/1.0'})
    with urllib.request.urlopen(request,timeout=150) as response:
        data=json.load(response)
    if not isinstance(data,dict) or not isinstance(data.get(key),list) or len(data[key])<1000:
        raise ValueError('Invalid Cardmarket data: '+name)
    (dist/'data'/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf8')
    print(name,len(data[key]))
(dist/'index.html').write_bytes((root/'index.html').read_bytes())
(dist/'.nojekyll').write_text('')
