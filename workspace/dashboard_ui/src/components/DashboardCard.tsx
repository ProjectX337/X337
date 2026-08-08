interface DashboardCardProps {

    title: string;

    value: string | number;

}



export default function DashboardCard(
    {
        title,
        value
    }: DashboardCardProps
){

    return (

        <div
            style={{
                border:"1px solid #333",
                borderRadius:"12px",
                padding:"20px",
                margin:"10px",
                minWidth:"180px"
            }}
        >

            <h3>
                {title}
            </h3>


            <p
                style={{
                    fontSize:"32px"
                }}
            >
                {value}
            </p>


        </div>

    );

}
