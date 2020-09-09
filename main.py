from requests.api import get
import get_cover
if __name__ == "__main__":
    ab_id = input('请输入AV/BVid:')
    json = get_cover.run(ab_id)
    print(f"BV号：{json['bvid']}\n封面地址：{json['cover_link']}")
    input('按任意键退出')
        
