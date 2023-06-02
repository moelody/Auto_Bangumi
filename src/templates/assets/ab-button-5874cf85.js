import{l as d,_ as k,a4 as f,a0 as c,aL as C,a1 as h,d as m,a5 as w,a6 as y,aM as $,a9 as B,aa as T,R as l,al as N,aN as R,o as b,c as L,a as V,t as j,U as v,i as D,w as g,b as O,g as u,n as P,j as W}from"./index-ce25b577.js";function H(e,t){return d(()=>{for(const n of t)if(e[n]!==void 0)return e[n];return e[t[t.length-1]]})}const I=e=>{const{opacityDisabled:t,heightTiny:n,heightSmall:s,heightMedium:i,heightLarge:a,heightHuge:o,primaryColor:r,fontSize:p}=e;return{fontSize:p,textColor:r,sizeTiny:n,sizeSmall:s,sizeMedium:i,sizeLarge:a,sizeHuge:o,color:r,opacitySpinning:t}},M={name:"Spin",common:k,self:I},E=M,K=f([f("@keyframes spin-rotate",`
 from {
 transform: rotate(0);
 }
 to {
 transform: rotate(360deg);
 }
 `),c("spin-container",{position:"relative"},[c("spin-body",`
 position: absolute;
 top: 50%;
 left: 50%;
 transform: translateX(-50%) translateY(-50%);
 `,[C()])]),c("spin-body",`
 display: inline-flex;
 align-items: center;
 justify-content: center;
 flex-direction: column;
 `),c("spin",`
 display: inline-flex;
 height: var(--n-size);
 width: var(--n-size);
 font-size: var(--n-size);
 color: var(--n-color);
 `,[h("rotate",`
 animation: spin-rotate 2s linear infinite;
 `)]),c("spin-description",`
 display: inline-block;
 font-size: var(--n-font-size);
 color: var(--n-text-color);
 transition: color .3s var(--n-bezier);
 margin-top: 8px;
 `),c("spin-content",`
 opacity: 1;
 transition: opacity .3s var(--n-bezier);
 pointer-events: all;
 `,[h("spinning",`
 user-select: none;
 -webkit-user-select: none;
 pointer-events: none;
 opacity: var(--n-opacity-spinning);
 `)])]),U={small:20,medium:18,large:16},X=Object.assign(Object.assign({},y.props),{description:String,stroke:String,size:{type:[String,Number],default:"medium"},show:{type:Boolean,default:!0},strokeWidth:Number,rotate:{type:Boolean,default:!0},spinning:{type:Boolean,validator:()=>!0,default:void 0}}),Y=m({name:"Spin",props:X,setup(e){const{mergedClsPrefixRef:t,inlineThemeDisabled:n}=w(e),s=y("Spin","-spin",K,E,e,t),i=d(()=>{const{size:o}=e,{common:{cubicBezierEaseInOut:r},self:p}=s.value,{opacitySpinning:z,color:_,textColor:x}=p,S=typeof o=="number"?$(o):p[B("size",o)];return{"--n-bezier":r,"--n-opacity-spinning":z,"--n-size":S,"--n-color":_,"--n-text-color":x}}),a=n?T("spin",d(()=>{const{size:o}=e;return typeof o=="number"?String(o):o[0]}),i,e):void 0;return{mergedClsPrefix:t,compitableShow:H(e,["spinning","show"]),mergedStrokeWidth:d(()=>{const{strokeWidth:o}=e;if(o!==void 0)return o;const{size:r}=e;return U[typeof r=="number"?"medium":r]}),cssVars:n?void 0:i,themeClass:a==null?void 0:a.themeClass,onRender:a==null?void 0:a.onRender}},render(){var e,t;const{$slots:n,mergedClsPrefix:s,description:i}=this,a=n.icon&&this.rotate,o=(i||n.description)&&l("div",{class:`${s}-spin-description`},i||((e=n.description)===null||e===void 0?void 0:e.call(n))),r=n.icon?l("div",{class:[`${s}-spin-body`,this.themeClass]},l("div",{class:[`${s}-spin`,a&&`${s}-spin--rotate`],style:n.default?"":this.cssVars},n.icon()),o):l("div",{class:[`${s}-spin-body`,this.themeClass]},l(N,{clsPrefix:s,style:n.default?"":this.cssVars,stroke:this.stroke,"stroke-width":this.mergedStrokeWidth,class:`${s}-spin`}),o);return(t=this.onRender)===null||t===void 0||t.call(this),n.default?l("div",{class:[`${s}-spin-container`,this.themeClass],style:this.cssVars},l("div",{class:[`${s}-spin-content`,this.compitableShow&&`${s}-spin-content--spinning`]},n),l(R,{name:"fade-in-transition"},{default:()=>this.compitableShow?r:null})):r}}),q={flex:"~ items-start","justify-between":""},J=m({__name:"ab-label",props:{label:{default:""}},setup(e){return(t,n)=>(b(),L("div",q,[V("div",null,j(t.label),1),v(t.$slots,"default")]))}}),A=m({__name:"ab-button",props:{type:{default:"primary"},size:{default:"normal"},link:{default:null},loading:{type:Boolean,default:!1}},emits:["click"],setup(e){const t=e,n=d(()=>{switch(t.size){case"big":return"rounded-10px text-h1 w-276px h-55px text-h1";case"normal":return"rounded-6px w-170px h-36px";case"small":return"rounded-6px w-86px h-28px text-main"}}),s=d(()=>{switch(t.size){case"big":return"large";case"normal":return"small";case"small":return 18}});return(i,a)=>(b(),D(W(i.link!==null?"a":"button"),{href:i.link,"text-white":"","outline-none":"","f-cer":"",class:P([`type-${i.type}`,u(n)]),onClick:a[0]||(a[0]=o=>i.$emit("click"))},{default:g(()=>[O(u(Y),{show:i.loading,size:u(s)},{default:g(()=>[v(i.$slots,"default",{},void 0,!0)]),_:3},8,["show","size"])]),_:3},8,["href","class"]))}});const F=(e,t)=>{const n=e.__vccOpts||e;for(const[s,i]of t)n[s]=i;return n},Q=F(A,[["__scopeId","data-v-b927551b"]]);export{Q as _,J as a};
