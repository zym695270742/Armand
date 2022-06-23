<template>
<div style="height: 100%;">
  <el-container style="height: 100%;">
    <el-aside width="200px">
      <Menu></Menu>
    </el-aside>
    <el-container>
      <el-header style="line-height: 60px;">
          <el-input
              placeholder="请输入项目名称关键字，可模糊匹配"
              prefix-icon="el-icon-search"
              v-model="keys"
              @change="search_project">
          </el-input>
      </el-header>
      <el-main>

           <el-table
              :data="proj_list_data"
              stripe
              style="width: 100%">
              <el-table-column
                prop="id"
                label="项目编号"
                width="100">
              </el-table-column>
              <el-table-column
                prop="proj_name"
                label="项目名称"
                width="180">
              </el-table-column>
              <el-table-column
                prop="des"
                label="项目描述">
              </el-table-column>
              <el-table-column
                prop="creator_name"
                label="创建者"
                width="100">
              </el-table-column>
              <el-table-column
                prop="updator_name"
                label="更新者"
                width="100">
              </el-table-column>
             <el-table-column
                prop="create_time"
                label="创建时间"
                width="200">
              </el-table-column>
              <el-table-column
                prop="update_time"
                label="更新时间"
                width="200">
              </el-table-column>
              <el-table-column>
                  <template slot="header">
                          <el-button @click="add_proj()" style="width: 121px">新增项目</el-button>
                  </template>
                  <template slot-scope="scope">
                      <router-link :to="'/proj_detail?proj_id='+scope.row.id">
                          <el-button
                            type="primary"
                            size="small">查看</el-button>
                      </router-link>
                      &nbsp;
                      <el-button
                          @click="delete_proj(scope.row.id)"
                          type="danger"
                          size="small">删除</el-button>
                  </template>

              </el-table-column>
          </el-table>

      </el-main>
    </el-container>
  </el-container>
</div>
</template>

<script>
import Menu from '../components/Menu.vue'
import axios from 'axios'
export default {
  name: "project_list",
  data(){
    return{
      keys:'',
      proj_list_data:[],
    }
  },
  methods:{
    search_project(){
      axios.get('http://localhost:8000/proj_list/',{
        params:{
          keys: this.keys
        }}).then(res=>{
          this.proj_list_data = res.data
      })
    },
    add_proj(){
      axios.get('http://localhost:8000/add_proj/').then(res=>{
        this.proj_list_data = res.data
      })
    },
    delete_proj(proj_id){
      axios.get('http://localhost:8000/delete_proj/',{  // url最后必须加上’/‘，否则报跨域错误
        params:{
          proj_id: proj_id
        }
      }).then(res=>{
        this.proj_list_data = res.data
      })
    }
  },
  components:{
    Menu,
  },
  mounted:function(){
    axios.get('http://localhost:8000/proj_list/').then(res=>{
      this.proj_list_data = res.data
    });
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