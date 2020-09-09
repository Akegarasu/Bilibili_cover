# Bilibili_cover
一个快速根据av/bv号提取bilibili封面真实链接的库 同时支持av/bv号转换

##使用方法

    import get_cover
    #方法1
    get_cover.fast_run('av/bvid')
    #返回值：图片真实链接
    #方法1
    get_cover.run('av/bvid')
    #返回值：字典{'bvid','avid','cover_link'}