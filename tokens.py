import uuid
import random
import hashlib
import httpx
import time

class Tokens():
    def Cooki(self):
        try:
            self.headers = {
                'x-ig-app-locale': 'en_US',
                'x-ig-device-locale': 'en_US',
                'x-ig-mapped-locale': 'en_US',
                'x-pigeon-session-id': self.Pigionid,
                'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
                'X-Ig-Bandwidth-Speed-Kbps': f'{random.randint(1000, 9999)}.000',
                'X-Ig-Bandwidth-Totalbytes-B': f'{random.randint(10000000, 99999999)}',
                'X-Ig-Bandwidth-Totaltime-Ms': f'{random.randint(10000, 99999)}',
                'x-bloks-version-id': self.Block,
                'x-ig-www-claim': '0',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': self.Deviceid,
                'x-ig-family-device-id': self.FDeviceid,
                'x-ig-android-id': self.Androidid,
                'x-ig-timezone-offset': '-18000',
                'x-fb-connection-type': 'WIFI',
                'x-ig-connection-type': 'WIFI',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-app-id': '567067343352427',
                'priority': 'u=3',
                'user-agent': self.Useragent,
                'accept-language': 'en-US',
                'ig-intended-user-id': '0',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
            }

            data = {
                'normal_token_hash': '',
                'device_id': self.Androidid,
                'custom_device_id': self.Deviceid,
                'fetch_reason': 'token_expired',
            }


            response = httpx.post('https://b.i.instagram.com/api/v1/zr/dual_tokens/', headers=self.headers, data=data)
            self.Mid=response.headers['ig-set-x-mid']
            self.headers.update({'X-Mid': str(self.Mid), })

            data = {
                'params': '{"show_internal_settings":false,"offline_experiment_group":"caa_iteration_v3_perf_ig_4","device_id":"'+str(self.Androidid)+'","logged_out_user":"","qe_device_id":"'+str(self.Deviceid)+'","qpl_join_id":"'+str(self.qpl_join_id)+'","family_device_id":"'+str(self.FDeviceid)+'","waterfall_id":"'+str(self.Waterid)+'","account_list":[{"token":"","account_type":"google_oauth"},{"token":"","account_type":"google_oauth"}],"blocked_uid":[],"INTERNAL_INFRA_THEME":"default"}',
                'bk_client_context': '{"bloks_version":"'+str(self.Block)+'","styles_id":"instagram"}',
                'bloks_versioning_id': str(self.Block),
            }
            updict = {
                "Content-Length": str(len(data)),
                'Host': 'i.instagram.com',
                'X-Mid': str(self.Mid),
                'X-Ig-Family-Device-Id': str(self.FDeviceid),
                'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),

            }
            self.headers = {key: updict.get(key, self.headers[key]) for key in self.headers}

            response = httpx.post(
                'https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.process_client_data_and_redirect/',
                headers=self.headers,
                data=data,
            )
            self.Elgn = response.text.split('"K":"email","!":"')[1].split('","":[{"㚱":{"9":"","2":""}}]')[0]
            self.Plgn = response.text.split('"K":"password","!":"')[1].split('","":[{"㚱":{"9":"","2":""}}]')[0]
            self.Insid = response.text.split(', (bk.action.i32.Const, 2), (bk.action.tree.Make, (bk.action.i32.Const, 13704))))), (bk.action.i32.Const, 35), (bk.action.core.FuncConst, (bk.action.core.TakeLast, (bk.action.qpl.MarkerPoint, (bk.action.i32.Const, 36707139), (bk.action.i32.Const, ')[1].split(r'), \"handle_async_action_result_start\", (bk.action.tree.Make, (bk.action.i32.Const, 13747))), (bk.action.core.TakeLast, (bk.action.core.TakeLast, (bk.action.bloks.WriteLocalState, \"')[0]
            self.Mkrid = response.text.split(r'\")))), (bk.action.core.TakeLast, (bk.action.bloks.WriteGlobalConsistencyStore, \"CAA_LOGIN_FORM:is_login_pending:0\", (bk.action.bool.Const, true)), (bk.action.core.TakeLast, (bk.action.qpl.MarkerStartV2, (bk.action.i32.Const, ')[1].split('), (bk.action.i32.Const, ')[0]

            return self.Mid,self.Elgn,self.Plgn,self.Insid,self.Mkrid,self.headers
        except Exception as e:
            print(e)
            Tokens.Cooki(self)

    def Cooki2(self):
        try:

            data = {
                'normal_token_hash': '',
                'device_id': self.Androidid,
                '_uuid': self.Deviceid,
                'custom_device_id': self.Deviceid,
                'fetch_reason': 'token_expired',
            }
            self.headers.update({
                'Authorization': f'Bearer IGT:2:{self.bearer}',
                'Ig-U-Ds-User-Id': str(self.UserId),
                'Ig-U-Rur': self.rur,
            })
            updict = {
                "Content-Length": str(len(data)),
                'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
                'Ig-Intended-User-Id': str(self.UserId),
                'Host': 'b.i.instagram.com',

            }
            headers = {key: updict.get(key, self.headers[key]) for key in self.headers}
            response = httpx.post('https://b.i.instagram.com/api/v1/zr/dual_tokens/', headers=self.headers,
                                     data=data)
            self.claim = response.headers['x-ig-set-www-claim']
            self.shbid = response.headers['ig-set-ig-u-shbid']
            self.igid = self.shbid.split(',')[0]
            self.shbts = response.headers['ig-set-ig-u-shbts']
            self.urur = response.headers['ig-set-ig-u-rur'].split(':')[1]

            return self.claim,self.shbts,self.igid,self.shbts,self.urur
        except Exception as e:
            print(e)
            Tokens.Cooki2(self)




