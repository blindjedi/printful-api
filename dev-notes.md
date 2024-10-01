## Tasks

1. Connect to the Printful API
2. Get a list of products
    1. find a product by name (ts, hoodie, mug, etc.)
3. Get a list of variants for a product

File ID: 746398768 - brek
File ID: 746478538 - gaia

Product created successfully: {'code': 200, 'result': {'id': 361834414, 'external_id': '66fb2063b841f6', 'name': 'Custom
Black Map T-Shirt', 'variants': 3, 'synced': 3, 'thumbnail_url': None, 'is_ignored': False}, 'extra': []}


## tutorial in v2
Product found: Unisex Staple T-Shirt | Bella + Canvas 3001 (ID: 71)
```python
catalog_product = \
    {'brand': 'Bella + Canvas',
     'catalog_url': 'https://www.printful.com/custom/mens/t-shirts/unisex-staple-t-shirt-bella-canvas-3001',
     'category_id': 24, 'currency': 'USD',
     'description': "<span class='wysiwyg pf-d-block'><p>The Unisex Staple T-Shirt feels soft and light with just the right amount of stretch. It'...roduct sourced from Nicaragua, Mexico, Honduras, or the US</li></ul><p>This product is made on demand. No minimums.</p></span>",
     'display_name': 'Unisex Staple T-Shirt | Bella + Canvas 3001',
     'environmental_qualities': '<span class=\'wysiwyg pf-d-block\'><ul>\n<li style="font-weight:400;"><span style="font-weight:400;">Traceability:</span><ul>...shipment-"><span style="font-weight:400;">Packaging compostability and recyclability information</span></a></li>\n</ul></span>',
     'id': 71,
     'image_url': 'https://files.cdn.printful.com/o/upload/product-catalog-img/20/2079a3ee4cc472ad952fe16654f274cd_l',
     'price': 11.5
     }
```