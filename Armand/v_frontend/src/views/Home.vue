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
              <el-header style="text-align: left;padding: 10px;height: 80px;">
                <el-row :gutter="5" style="margin-top: 5px">
                  <el-col :span="6">
                    <div class="staticbanner" style="background: #409eff">
                      <div class="title">
                        <p>官方接口：{{ real_time_datas.ApiShop_count}}</p>
                        <el-tag size="mini" style="color: #409eff">实时</el-tag>
                      </div>
                    </div>
                  </el-col>

                  <el-col :span="6">
                    <div class="staticbanner" style="background: #d26f32">
                      <div class="title">
                        <p>未读消息：{{ real_time_datas.UnReadNews_count}}</p>
                        <el-tag size="mini" style="color: #d26f32">实时</el-tag>
                      </div>
                    </div>
                  </el-col>

                  <el-col :span="6">
                    <div class="staticbanner" style="background: #67c23a">
                      <div class="title">
                        <p>用例执行结果：{{ real_time_datas.RunCase_count}}</p>
                        <el-tag size="mini" style="color: #67c23a">实时</el-tag>
                      </div>
                    </div>
                  </el-col>

                  <el-col :span="6">
                    <div class="staticbanner" style="background: #707070">
                      <div class="title">
                        <p>导入接口次数：{{ real_time_datas.Import_count}}</p>
                        <el-tag size="mini" style="color: #707070">实时</el-tag>
                      </div>
                    </div>
                  </el-col>
                </el-row>
              </el-header>
              <el-main>

                <el-card class="box-card" style="overflow-y: auto;width: 30%;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>All Projects</span>
                    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                  </div>
                  <p>项目总数：{{ tj_datas.overview.project_count}}</p>
                  <p>接口总数：{{ tj_datas.overview.api_count}}</p>
                  <p>环境总数：{{ tj_datas.overview.env_count}}</p>
                  <p>用例总数：{{ tj_datas.overview.case_count}}</p>
                  <p>用户总数：{{ tj_datas.overview.user_count}}</p>
                </el-card>


                <el-card class="box-card" style="width:-webkit-calc(70%  - 24px) ;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>上次监控情况</span>
                    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                  </div>
                  <span style="font-size: xx-small">用例通过率</span>
                  <el-progress :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitors.case_pass" status="success" style="margin-bottom: 10px"></el-progress>
                  <span style="font-size: xx-small">接口通过率</span>
                  <el-progress :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitors.api_pass" status="exception" style="margin-bottom: 10px"></el-progress>
                  <span style="font-size: xx-small">用例失败/报错率</span>
                  <el-progress :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitors.case_fail" style="margin-bottom: 10px"></el-progress>
                </el-card>

                <!--    second line cards            -->
                <el-card class="box-card" style="width:-webkit-calc(70%  - 24px) ;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>个人贡献</span>
                    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
                  </div>
                  <table class="table">
                    <thead>
                      <th><el-progress type="circle" :percentage="tj_datas.contributions.project"></el-progress></th>
                      <th><el-progress type="circle" :percentage="tj_datas.contributions.case"></el-progress></th>
                      <th><el-progress type="circle" :percentage="tj_datas.contributions.api" color="rgb(19, 206, 102)"></el-progress></th>
                      <th><el-progress type="circle" :percentage="tj_datas.contributions.monitor" color="#f56c6c"></el-progress></th>
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
                  <div v-for="o in tj_datas.news" class="text item">
                    {{ o.from_user_name + '消息： ' + o.content }}
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
import Menu from '../components/Menu.vue'
import axios from 'axios'
export default {
  name: 'home',
  data(){
    return{
      message: 'default data',
      tj_datas:{
        notices:[],
        news:[],
        overview:{
          project_count:0,
          api_count:0,
          case_count:0,
          env_count:0,
          user_count:0
        },
        monitors:{
          case_pass:0,
          api_pass:0,
          case_fail:0
        },
        contributions:{
          project:0,
          case:0,
          api:0,
          monitor:0
        }
      },
      real_time_datas:{
        ApiShop_count: 0,
        UnReadNews_count: 0,
        RunCase_count: 0,
        Import_count: 0,
      }
    };
  },
  methods:{

  },
  components:{
    Menu,
  },
  mounted:function () {
    axios('http://localhost:8000/get_tj_datas/').then(res=>{
      this.tj_datas = res.data;
    });
    axios.get('http://localhost:8000/get_real_time_datas/').then(
        res=>{
          this.real_time_datas = res.data
        });

    setInterval(()=>{
      axios.get('http://localhost:8000/get_real_time_datas/').then(
          res=>{
            this.real_time_datas = res.data
          }
      )},1000000
    )
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
    overflow-y:auto;
    border: 0px;
  }

  th,td{
    text-align: center;
    font-size: xx-small;
    width: 20%;
  }

/*  el- row*/
  .staticbanner{
    color: white;
    height: 50px;
    border-radius: 3px;
    padding: 0 8px;
  }
  .title{
    /*弹性伸缩盒子*/
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  p{
    font-size: 13px;
    font-weight: bold;
  }
</style>