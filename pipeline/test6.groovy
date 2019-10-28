//var
def cur_date = new Date().format('yyyyMMddHHmmss')
def cur_name = "${cur_date}"+"_"+"${BUILD_NUMBER}"+"_"+"${dev}"
//def_slack
def slack_notify = true

def notifyBuild(slack_notify, buildStatus, msg) {
    buildStatus =  buildStatus ?: 'SUCCESSFUL'

    def colorName = 'RED'
    def colorCode = '#FF0000'
    def subject = "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"
    def summary = "${subject} (${env.BUILD_URL})" + "\n"

    if (buildStatus == 'STARTED') {
        color = 'YELLOW'
        colorCode = '#FFFF00'
        summary += "${msg}"
    } else if (buildStatus == 'SUCCESSFUL') {
        color = 'GREEN'
        colorCode = '#00FF00'
        summary += "${msg}"
    } else {
        color = 'RED'
        colorCode = '#FF0000'
        summary += "${msg}"
    }
    if (slack_notify){
    slackSend (color: colorCode, message: summary)
    }
}
//step
node {
    timestamps {
        ansiColor('xterm') {
            stage ('step-1') {
                echo "step-1-1"
                echo "${cur_date}"+"${dev}"
                //rm -f $workspace
            }//1

            stage ('step-2') {
                echo "step-2-2"
                echo "${cur_date}"+"${JOB_URL}"
                git 'https://github.com/DDanilov77/freecode.git'
            }//2

            stage ('step-3') {
                echo "step-3-3-3"
                echo "${cur_date}"+"${BUILD_NUMBER}"
                sh label: '3', script: """ 
                    DATE=\$( date "+%Y%m%d%H%M%S" )
                    VER="\${DATE}_\${BUILD_NUMBER}"
                    echo "VER: \$VER"
                    ls -la bash/*
                """
            }//3

            stage ('step-4') {
                echo "step-4-4-4-4"
                echo "${cur_date}"
                sh label: '4', script: """ 
                    DATE=\$( date "+%Y%m%d%H%M%S" )
                    VER="\${DATE}_\${BUILD_NUMBER}"
                    echo "VER: \$VER"
                    tar -cvf freecode.tar *
                """
            }//4

            stage ('step-5') {
                echo "step-5-5-5-5-5"
                echo "${cur_date}"
                sh label: '4', script: """ 
                    DATE=\$( date "+%Y%m%d%H%M%S" )
                    VER="\${DATE}_\${BUILD_NUMBER}"
                    echo "VER: \$VER"
                    mv freecode.tar freecode_\$VER.tar
                    mv freecode_\$VER.tar \${wdir}
                """
            }//5
        }//end_ansiColor
    }//end_timestamps
}//end_node
