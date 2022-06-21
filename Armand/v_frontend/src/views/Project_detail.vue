<template>
<div style="height: 100%;">
  <el-container style="height: 100%;">
    <el-aside width="200px">
          <Menu></Menu>
    </el-aside>
    <el-main>
          <span style="float:right;">项目ID: {{$route.query.proj_id}}</span>
          <el-tabs v-model="tab_name">
              <el-tab-pane label="项目配置" name="proj_detail_01">
                    <Proj_config :proj_id="$route.query.proj_id"></Proj_config>
              </el-tab-pane>
              <el-tab-pane label="项目用例" name="proj_detail_02">
                    <Proj_cases></Proj_cases>
              </el-tab-pane>
          </el-tabs>
    </el-main>
  </el-container>
</div>
</template>

<script>
import Menu from '../components/Menu.vue'
import axios from 'axios'
import Proj_config from '../components/Proj_config.vue'
import Proj_cases from '../components/Proj_cases.vue'
export default {
  name: "project_detail",
  data(){
    return{
      tab_name: "proj_detail_01",
    }
  },
  methods:{

  },
  components:{
    Menu,
    Proj_config,
    Proj_cases,
  },
  mounted:function(){

  }
}
</script>

<style scoped>
  .el-header {
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

</style>