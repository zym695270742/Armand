<template style="height: 100%;">
  <div class="home" style="height: 100%; ">
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <div style="height: 100%;">
          <el-container style="height: 100%;">
            <el-aside width="200px">
              <Menu></Menu>
            </el-aside>
            <el-container>
              <el-header>Header</el-header>
              <el-main>

                <el-card class="box-card" style="overflow-y: auto;width: 30%;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>All Projects</span>
                    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                  </div>
                  <p>项目总数：</p>
                  <p>接口总数：</p>
                  <p>用例总数：</p>
                  <p>用户总数：</p>
                </el-card>


                <el-card class="box-card" style="width:-webkit-calc(70%  - 24px) ;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>上次监控情况</span>
                    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                  </div>
                  <span style="font-size: xx-small">用例失败/成功比</span>
                  <el-progress :text-inside="true" :stroke-width="15" :percentage="70" style="margin-bottom: 10px"></el-progress>
                   <span style="font-size: xx-small">用例通过率</span>
                  <el-progress :text-inside="true" :stroke-width="15" :percentage="100" status="success" style="margin-bottom: 10px"></el-progress>
                  <span style="font-size: xx-small">接口通过率</span>
                  <el-progress :text-inside="true" :stroke-width="15" :percentage="50" status="exception" style="margin-bottom: 10px"></el-progress>
                </el-card>

                <!--    second line cards            -->
                <el-card class="box-card" style="width:-webkit-calc(70%  - 24px) ;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>个人贡献</span>
                    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                  </div>
                  <table class="table">
                    <thead>
                      <th><el-progress type="circle" :percentage="0"></el-progress></th>
                      <th><el-progress type="circle" :percentage="25"></el-progress></th>
                      <th><el-progress type="circle" :percentage="100" color="rgb(19, 206, 102)"></el-progress></th>
                      <th><el-progress type="circle" :percentage="70" color="#f56c6c"></el-progress></th>
                    </thead>
                    <tbody>
                      <td><span>个人项目占比</span></td>
                      <td><span>个人用例占比</span></td>
                      <td><span>个人接口占比</span></td>
                      <td><span>个人监控贡献占比</span></td>
                    </tbody>
                  </table>

                </el-card>


                <el-card class="box-card" style="overflow-y: auto;width: 30%;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>您的消息/任务</span>
                    <el-button style="float: right; padding: 3px 0" type="text">进入详情</el-button>
                  </div>
                  <div v-for="o in 10" class="text item">
                    {{'消息： ' + o }}
                  </div>
                </el-card>

              </el-main>
              <el-footer style="padding: 80px;text-align: left;padding: 0;height: 15%;">

                <el-card class="box-card" style="overflow-y: auto;min-height: 100%;width:100%;    background: linear-gradient(to left, #fbc2eb 0%, #a6c1ee 100%);">
                  <div v-for="o in tj_datas.notices" class="text item">
                    {{'平台更新日志： ' + o.content }}
                  </div>
                </el-card>

              </el-footer>
            </el-container>
          </el-container>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import Menu from '../components/Menu.vue'
import axios from 'axios'
export default {
  name: 'home',
  data(){
    return{
      tj_datas:{
        notices:[]
      }
    };
  },
  methods:{

  },
  components:{
    Menu,
  },
  mounted:function () {
    axios('http://127.0.0.1:8000/get_tj_datas/').then(res=>{
      this.tj_datas = res.data;
    })
  }

}
</script>

<style>
  .el-header, .el-footer {
    background: linear-gradient(to right, #fbc2eb 0%, #a6c1ee 100%);
    color: #333;
    text-align: center;
    line-height: 15px;
  }

  .el-aside {
    background: linear-gradient(to left, #fbc2eb 0%, #a6c1ee 100%);
    color: #333;
  }

  .el-main {
    color: #333;
  }


  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }


/*  card*/

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 10px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    /*height: 100%;*/
    max-height: 48%;
    min-height: 48%;
  }
  .el-card {
    background-color: white;
    text-align: left;
    margin-bottom: 10px;
    overflow-y:auto;
    border: 0px;
  }

  th,td{
    text-align: center;
    font-size: xx-small;
    width: 20%;
  }
</style>