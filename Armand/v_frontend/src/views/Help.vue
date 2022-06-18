<template style="height: 100%;">
  <div style="height: 100%; ">
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <div style="height: 100%;">
          <el-container style="height: 100%;">
            <el-aside width="200px">
              <Menu></Menu>
            </el-aside>
            <el-container>
              <el-header style="text-align: left;padding: 10px;height: 80px;">

              </el-header>
              <el-main>

                <el-card class="box-card" style="width:-webkit-calc(70%  - 24px) ;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>双向绑定测试</span>
                  </div>
                  <input v-model="message" placeholder="edit me" />
                  <p>Message1 is: {{ message }}</p>
                  <input v-model="message" placeholder="edit me" />
                  <p>Message2 is: {{ message }}</p>
                </el-card>

                <!--    second line cards            -->
                <el-card class="box-card" style="width:-webkit-calc(70%  - 24px) ;float:left; margin-left: 10px;">
                  <div slot="header" class="clearfix">
                    <span>card2</span>
                    <el-button style="float: right; padding: 3px 0" type="text">xxxx</el-button>
                  </div>

                </el-card>


              </el-main>
              <el-footer style="padding: 80px;text-align: left;padding: 0;height: 15%;">
              </el-footer>
            </el-container>
          </el-container>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
import Menu from '../components/Menu.vue'
export default {
  name: 'Help',
  data() {
    return {
      message: 'default data',
    };
  },
  components:{
    Menu,
  },

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