import{_ as Q}from"./ab-button-5874cf85.js";import{d as m,r as x,p as A,l as T,m as H,q as V,k as Y,v as z,o as y,i as h,w as g,a as f,b as d,g as i,t as Z,j as ee,n as te,G as oe,W as ne,U as ae,M as se,X as le,D as L,x as M,J as pe,L as O,c as w,F as C,h as $,V as v,E as G}from"./index-ce25b577.js";import{u as j,o as D,c as re,l as I,H as E,t as q,b as ce,p as ie,N as R,e as P,U as ue,D as de,g as K}from"./ab-setting.vue_vue_type_script_setup_true_lang-8c5ee8cf.js";var _e=(t=>(t[t.Open=0]="Open",t[t.Closed=1]="Closed",t))(_e||{});let F=Symbol("DisclosureContext");function B(t){let n=z(F,null);if(n===null){let o=new Error(`<${t} /> is missing a parent <Disclosure /> component.`);throw Error.captureStackTrace&&Error.captureStackTrace(o,B),o}return n}let W=Symbol("DisclosurePanelContext");function ye(){return z(W,null)}let fe=m({name:"Disclosure",props:{as:{type:[Object,String],default:"template"},defaultOpen:{type:[Boolean],default:!1}},setup(t,{slots:n,attrs:o}){let l=x(t.defaultOpen?0:1),e=x(null),c=x(null),p={buttonId:x(null),panelId:x(null),disclosureState:l,panel:e,button:c,toggleDisclosure(){l.value=j(l.value,{[0]:1,[1]:0})},closeDisclosure(){l.value!==1&&(l.value=1)},close(s){p.closeDisclosure();let r=(()=>s?s instanceof HTMLElement?s:s.value instanceof HTMLElement?D(s):D(p.button):D(p.button))();r==null||r.focus()}};return A(F,p),re(T(()=>j(l.value,{[0]:I.Open,[1]:I.Closed}))),()=>{let{defaultOpen:s,...r}=t,a={open:l.value===0,close:p.close};return E({theirProps:r,ourProps:{},slot:a,slots:n,attrs:o,name:"Disclosure"})}}}),ge=m({name:"DisclosureButton",props:{as:{type:[Object,String],default:"button"},disabled:{type:[Boolean],default:!1},id:{type:String,default:()=>`headlessui-disclosure-button-${q()}`}},setup(t,{attrs:n,slots:o,expose:l}){let e=B("DisclosureButton");H(()=>{e.buttonId.value=t.id}),V(()=>{e.buttonId.value=null});let c=ye(),p=T(()=>c===null?!1:c.value===e.panelId.value),s=x(null);l({el:s,$el:s}),p.value||Y(()=>{e.button.value=s.value});let r=ce(T(()=>({as:t.as,type:n.type})),s);function a(){var _;t.disabled||(p.value?(e.toggleDisclosure(),(_=D(e.button))==null||_.focus()):e.toggleDisclosure())}function u(_){var U;if(!t.disabled)if(p.value)switch(_.key){case P.Space:case P.Enter:_.preventDefault(),_.stopPropagation(),e.toggleDisclosure(),(U=D(e.button))==null||U.focus();break}else switch(_.key){case P.Space:case P.Enter:_.preventDefault(),_.stopPropagation(),e.toggleDisclosure();break}}function b(_){switch(_.key){case P.Space:_.preventDefault();break}}return()=>{let _={open:e.disclosureState.value===0},{id:U,...X}=t,J=p.value?{ref:s,type:r.value,onClick:a,onKeydown:u}:{id:U,ref:s,type:r.value,"aria-expanded":t.disabled?void 0:e.disclosureState.value===0,"aria-controls":D(e.panel)?e.panelId.value:void 0,disabled:t.disabled?!0:void 0,onClick:a,onKeydown:u,onKeyup:b};return E({ourProps:J,theirProps:X,slot:_,attrs:n,slots:o,name:"DisclosureButton"})}}}),me=m({name:"DisclosurePanel",props:{as:{type:[Object,String],default:"div"},static:{type:Boolean,default:!1},unmount:{type:Boolean,default:!0},id:{type:String,default:()=>`headlessui-disclosure-panel-${q()}`}},setup(t,{attrs:n,slots:o,expose:l}){let e=B("DisclosurePanel");H(()=>{e.panelId.value=t.id}),V(()=>{e.panelId.value=null}),l({el:e.panel,$el:e.panel}),A(W,e.panelId);let c=ie(),p=T(()=>c!==null?(c.value&I.Open)===I.Open:e.disclosureState.value===0);return()=>{let s={open:e.disclosureState.value===0,close:e.close},{id:r,...a}=t,u={id:r,ref:e.panel};return E({ourProps:u,theirProps:a,slot:s,attrs:n,slots:o,features:R.RenderStrategy|R.Static,visible:p.value,name:"DisclosurePanel"})}}});const be={"rounded-10px":"","overflow-hidden":"","h-max":""},he={"text-h2":""},xe={line:"","my-12px":""},S=m({__name:"ab-fold-panel",props:{title:{default:"title"}},setup(t){return(n,o)=>(y(),h(i(fe),null,{default:g(({open:l})=>[f("div",be,[d(i(ge),{"bg-theme-row":"","w-full":"","text-white":"","fx-cer":"","px-20px":"","h-45px":"","justify-between":""},{default:g(()=>[f("div",he,Z(n.title),1),(y(),h(ee(l?i(ue):i(de)),{size:"24"}))]),_:2},1024),f("div",{"bg-white":"","py-20px":"",class:te([l?"px-20px":"px-8px"])},[oe(f("div",xe,null,512),[[ne,!l]]),d(i(me),null,{default:g(()=>[ae(n.$slots,"default")]),_:3})],2)])]),_:3}))}}),ve={"space-y-12px":""},we=m({__name:"config-player",setup(t){const{types:n,type:o,url:l}=se(le());return(e,c)=>{const p=K,s=S;return y(),h(s,{title:"Media Player Setting"},{default:g(()=>[f("div",ve,[d(p,{data:i(o),"onUpdate:data":c[0]||(c[0]=r=>L(o)?o.value=r:null),type:"select",label:"type",prop:{items:i(n)}},null,8,["data","prop"]),d(p,{data:i(l),"onUpdate:data":c[1]||(c[1]=r=>L(l)?l.value=r:null),type:"input",label:"url",prop:{placeholder:"media player url"}},null,8,["data"])])]),_:1})}}}),N={async getConfig(){const{data:t}=await M.get("api/v1/getConfig");return t},async updateConfig(t){const{data:n}=await M.post("api/v1/updateConfig",t);return n.message==="Success"}},Ke={program:{rss_time:0,rename_time:0,webui_port:0},downloader:{type:"qbittorrent",host:"",username:"",password:"",path:"",ssl:!1},rss_parser:{enable:!0,type:"mikan",token:"",custom_url:"",filter:[],language:"zh",parser_type:"parser"},bangumi_manage:{enable:!0,eps_complete:!0,rename_method:"normal",group_tag:!0,remove_bad_torrent:!0},log:{debug_enable:!1},proxy:{enable:!1,type:"http",host:"",port:0,username:"",password:""},notification:{enable:!1,type:"telegram",token:"",chat_id:""}},k=pe("config",()=>{const t=x(Ke),{execute:n,onResult:o}=O(N.getConfig);o(p=>{t.value=p});const{execute:l}=O(N.updateConfig,{failRule:p=>!p,message:{success:"Apply Success!",fail:"Apply Failed!"}}),e=()=>l(t.value);function c(p){return T(()=>t.value[p])}return{config:t,getConfig:n,setConfig:e,getSettingGroup:c}}),Se={"space-y-12px":""},ke=m({__name:"config-proxy",setup(t){const{getSettingGroup:n}=k(),o=n("proxy"),e=[{configKey:"enable",label:"Enable",type:"switch"},{configKey:"type",label:"Proxy Type",type:"select",prop:{items:["http","https","socks5"]},bottomLine:!0},{configKey:"host",label:"Host",type:"input",prop:{type:"text",placeholder:"127.0.0.1"}},{configKey:"port",label:"Port",type:"input",prop:{type:"text",placeholder:"7890"}},{configKey:"username",label:"Username",type:"input",prop:{type:"text",placeholder:"username"}},{configKey:"password",label:"Password",type:"input",prop:{type:"text",placeholder:"password"}}];return(c,p)=>{const s=K,r=S;return y(),h(r,{title:"Proxy Setting"},{default:g(()=>[f("div",Se,[(y(),w(C,null,$(e,a=>d(s,v({key:a.configKey},a,{data:i(o)[a.configKey],"onUpdate:data":u=>i(o)[a.configKey]=u}),null,16,["data","onUpdate:data"])),64))])]),_:1})}}}),De={"space-y-12px":""},Ce=m({__name:"config-notification",setup(t){const{getSettingGroup:n}=k(),o=n("notification"),e=[{configKey:"enable",label:"Enable",type:"switch",bottomLine:!0},{configKey:"type",label:"Type",type:"select",css:"w-140px",prop:{items:["telegram","server-chan","bark"]}},{configKey:"token",label:"Token",type:"input",prop:{type:"text",placeholder:"token"}},{configKey:"chat_id",label:"Chat ID",type:"input",prop:{type:"text",placeholder:"chat id"}}];return(c,p)=>{const s=K,r=S;return y(),h(r,{title:"Notification Setting"},{default:g(()=>[f("div",De,[(y(),w(C,null,$(e,a=>d(s,v({key:a.configKey},a,{data:i(o)[a.configKey],"onUpdate:data":u=>i(o)[a.configKey]=u}),null,16,["data","onUpdate:data"])),64))])]),_:1})}}}),$e={"space-y-12px":""},Pe=m({__name:"config-manage",setup(t){const{getSettingGroup:n}=k(),o=n("bangumi_manage"),e=[{configKey:"enable",label:"Enable",type:"switch"},{configKey:"rename_method",label:"Rename Method",type:"select",prop:{items:["normal","pn","advance","none"]},bottomLine:!0},{configKey:"eps_complete",label:"Eps complete",type:"switch"},{configKey:"group_tag",label:"Add Group Tag",type:"switch"},{configKey:"remove_bad_torrent",label:"Delete Bad Torrent",type:"switch"}];return(c,p)=>{const s=K,r=S;return y(),h(r,{title:"Manage Setting"},{default:g(()=>[f("div",$e,[(y(),w(C,null,$(e,a=>d(s,v({key:a.configKey},a,{data:i(o)[a.configKey],"onUpdate:data":u=>i(o)[a.configKey]=u}),null,16,["data","onUpdate:data"])),64))])]),_:1})}}}),Te={"space-y-12px":""},Ue=m({__name:"config-download",setup(t){const{getSettingGroup:n}=k(),o=n("downloader"),e=[{configKey:"type",label:"Downloader Type",type:"select",css:"w-115px",prop:{items:["qbittorrent"]}},{configKey:"host",label:"Host",type:"input",prop:{type:"text",placeholder:"127.0.0.1:8989"}},{configKey:"username",label:"Username",type:"input",prop:{type:"text",placeholder:"admin"}},{configKey:"password",label:"Password",type:"input",prop:{type:"text",placeholder:"admindmin"},bottomLine:!0},{configKey:"path",label:"Download Path",type:"input",prop:{type:"text",placeholder:"/downloads/Bangumi"}},{configKey:"ssl",label:"SSL",type:"switch"}];return(c,p)=>{const s=K,r=S;return y(),h(r,{title:"Downloader Setting"},{default:g(()=>[f("div",Te,[(y(),w(C,null,$(e,a=>d(s,v({key:a.configKey},a,{data:i(o)[a.configKey],"onUpdate:data":u=>i(o)[a.configKey]=u}),null,16,["data","onUpdate:data"])),64))])]),_:1})}}}),Ie={"space-y-12px":""},Ee=m({__name:"config-parser",setup(t){const{getSettingGroup:n}=k(),o=n("rss_parser"),p=[{configKey:"enable",label:"Enable",type:"switch"},{configKey:"type",label:"Source",type:"select",css:"w-115px",prop:{items:["mikan"]}},{configKey:"token",label:"Token",type:"input",prop:{type:"text",placeholder:"token"}},{configKey:"custom_url",label:"Custom Url",type:"input",prop:{type:"text",placeholder:"mikanime.tv"},bottomLine:!0},{configKey:"language",label:"Language",type:"select",prop:{items:["zh","en","jp"]}},{configKey:"parser_type",label:"Parser Type",type:"select",prop:{items:["tmdb","mikan","parser"]}},{configKey:"filter",label:"Exclude",type:"dynamic-tags"}];return(s,r)=>{const a=K,u=S;return y(),h(u,{title:"Parser Setting"},{default:g(()=>[f("div",Ie,[(y(),w(C,null,$(p,b=>d(a,v({key:b.configKey},b,{data:i(o)[b.configKey],"onUpdate:data":_=>i(o)[b.configKey]=_}),null,16,["data","onUpdate:data"])),64))])]),_:1})}}}),Be={"space-y-12px":""},Le=m({__name:"config-normal",setup(t){const{getSettingGroup:n}=k(),o=n("program"),l=n("log"),e=[{configKey:"rss_time",label:"Interval Time of Rss",type:"input",css:"w-72px",prop:{type:"number",placeholder:"port"}},{configKey:"rename_time",label:"Interval Time of Rename",type:"input",css:"w-72px",prop:{type:"number",placeholder:"port"}},{configKey:"webui_port",label:"WebUI Port",type:"input",css:"w-72px",prop:{type:"number",placeholder:"port"},bottomLine:!0}],c={configKey:"debug_enable",label:"Debug",type:"switch"};return(p,s)=>{const r=K,a=S;return y(),h(a,{title:"Normal Setting"},{default:g(()=>[f("div",Be,[(y(),w(C,null,$(e,u=>d(r,v({key:u.configKey},u,{data:i(o)[u.configKey],"onUpdate:data":b=>i(o)[u.configKey]=b}),null,16,["data","onUpdate:data"])),64)),d(r,v(c,{data:i(l)[c.configKey],"onUpdate:data":s[0]||(s[0]=u=>i(l)[c.configKey]=u)}),null,16,["data"])])]),_:1})}}}),Me={"h-full":"",flex:"~ col"},Oe={grid:"~ cols-2","gap-20px":"","mb-auto":""},Ge={"space-y-20px":""},je={"space-y-20px":""},Re={"fx-cer":"","justify-end":"","gap-8px":"","mt-20px":""},Ve=m({__name:"config",setup(t){const{getConfig:n,setConfig:o}=k();return n(),(l,e)=>{const c=Le,p=Ee,s=Ue,r=Pe,a=Ce,u=ke,b=we,_=Q;return y(),w("div",Me,[f("div",Oe,[f("div",Ge,[d(c),d(p),d(s),d(r)]),f("div",je,[d(a),d(u),d(b)])]),f("div",Re,[d(_,{type:"warn",onClick:i(n)},{default:g(()=>[G("Cancel")]),_:1},8,["onClick"]),d(_,{onClick:i(o)},{default:g(()=>[G("Apply")]),_:1},8,["onClick"])])])}}});export{Ve as default};
